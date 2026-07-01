"""Generate assets/map/world.svg from Natural Earth GeoJSON (one-off helper)."""
import json
import os
import urllib.request

GEO_URL = "https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson"
MEMBERS = {"Portugal", "Brazil", "Morocco", "France"}


def ring_to_path(ring):
    parts = []
    for i, (lon, lat) in enumerate(ring):
        x = (lon + 180) * (1000 / 360)
        y = (90 - lat) * (500 / 180)
        parts.append(f"{'M' if i == 0 else 'L'}{x:.1f} {y:.1f}")
    parts.append("Z")
    return " ".join(parts)


def feature_paths(geometry):
    if geometry["type"] == "Polygon":
        return [ring_to_path(geometry["coordinates"][0])]
    if geometry["type"] == "MultiPolygon":
        return [ring_to_path(poly[0]) for poly in geometry["coordinates"]]
    return []


def centroid(feature):
    coords = []
    geom = feature["geometry"]
    if geom["type"] == "Polygon":
        coords = geom["coordinates"][0]
    elif geom["type"] == "MultiPolygon":
        for poly in geom["coordinates"]:
            coords.extend(poly[0])
    lon = sum(c[0] for c in coords) / len(coords)
    lat = sum(c[1] for c in coords) / len(coords)
    x = (lon + 180) * (1000 / 360)
    y = (90 - lat) * (500 / 180)
    return x, y


def main():
    cache = os.path.join(os.environ.get("TEMP", "."), "world.geojson")
    if not os.path.exists(cache):
        urllib.request.urlretrieve(GEO_URL, cache)
    with open(cache, encoding="utf-8") as f:
        geo = json.load(f)

    land = []
    highlight = []
    marks = []

    for feature in geo["features"]:
        name = feature.get("properties", {}).get("name", "")
        paths = feature_paths(feature["geometry"])
        if not paths:
            continue
        d = " ".join(f'<path d="{p}"/>' for p in paths)
        if name in MEMBERS:
            highlight.append(d)
            marks.append(centroid(feature))
        else:
            land.append(d)

    rings = "\n".join(
        f'    <circle cx="{x:.1f}" cy="{y:.1f}" r="11"/>' for x, y in marks
    )
    dots = "\n".join(
        f'    <circle cx="{x:.1f}" cy="{y:.1f}" r="5.5"/>' for x, y in marks
    )

    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 500" fill="none" aria-hidden="true">
  <g fill="rgba(213,183,121,0.06)" stroke="#D5B779" stroke-width="0.45" stroke-linejoin="round" opacity="0.42">
    {"".join(land)}
  </g>
  <g fill="rgba(213,183,121,0.16)" stroke="#D5B779" stroke-width="0.85" stroke-linejoin="round" opacity="0.9">
    {"".join(highlight)}
  </g>
  <g class="map-marker-rings" fill="none" stroke="#D5B779" stroke-width="1" opacity="0.35">
{rings}
  </g>
  <g class="map-markers" fill="#D5B779">
{dots}
  </g>
</svg>
"""

    out = os.path.join(os.path.dirname(__file__), "..", "assets", "map", "world.svg")
    with open(out, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {out} ({len(svg)} bytes)")


if __name__ == "__main__":
    main()

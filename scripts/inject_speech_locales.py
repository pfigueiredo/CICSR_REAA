# -*- coding: utf-8 -*-
"""Clean OCR speech text into HTML fragments for locales."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Hand-cleaned from Docs/discursos PDFs (Lisboa, 4 Jul 2026)
SPEECH = {
    "pt": {
        "salutation": "Muito Poderosos Soberanos Grandes Comendadores,<br/>Meus Ilustres Irmãos,",
        "body": """
<p>Cumprir e fazer cumprir o Regulamento da Confederação Internacional dos Supremos Conselhos Soberanos e Regulares, hoje ratificado, é o compromisso que vou honrar e vou contribuir para que todos o honrem.</p>
<p>Nele consta que o SCP terá o primeiro mandato e é nessa qualidade que assumo hoje a presidência desta Confederação. Compreendo o contexto em que recebi a vossa eleição. É, pois, com humildade e responsabilidade acrescidas, sentido de serviço e a firme convicção de que só cumprirei esta missão se conseguir desenvolver consensos e aprofundar a confiança coletiva e recíproca iniciada e mantida ao longo destes últimos dois anos, em reuniões presenciais e virtuais, em França, Brasil, Marrocos e Portugal.</p>
<p>A força da Maçonaria sustenta-se no recrutamento seletivo e no desenvolvimento pessoal do maçon, contribuindo para a melhoria da Humanidade.</p>
<p>A força de um Supremo Conselho sustenta-se, por um lado, na evolução contínua dos seus membros, através da compreensão do que é a Consciência, ou seja, a capacidade de perceber-se a si mesmo e ao Contexto, envolvendo processos que permitem atenção, autoconsciência e absorção de informações na mente e, por outro, no reforço da espiritualidade de todos, abrindo portais para estados que transcendem a realidade ordinária.</p>
<p>A força de uma Confederação de Supremos Conselhos sustenta-se, não obstante as diferenças de estádios evolutivos, dimensão e cultura dos seus membros, na capacidade coletiva de integrar abordagens e atuações específicas de cada um, encontrando as áreas de reflexão e a forma de intervenção para a construção de consensos.</p>
<p>O R.E.A.A., através dos seus Rituais e dos Regulamentos de 1762 e de 1786, agrega-nos e propicia-nos propósitos comuns.</p>
<p>É neste contexto que proponho valores fundadores, fio-condutor da nossa atuação:</p>
<ul>
<li><strong>Tolerância e respeito</strong>, para transformar divergências de pontos de vista em diálogo fecundo.</li>
<li><strong>Fraternidade e solidariedade</strong>, para que ninguém fique para trás, dentro e fora dos nossos Supremos Conselhos.</li>
<li><strong>Integridade e discrição</strong>, porque a confiança é o cimento de qualquer obra duradoura.</li>
<li><strong>Busca da Verdade e aperfeiçoamento moral</strong>, o labor silencioso que dá sentido a tudo o resto.</li>
</ul>
<p>Sendo uma Confederação internacional, estes valores ganham novas exigências e novas oportunidades. Precisamos de uma liderança que escute, coordene e sirva. Liderar, neste enquadramento, é construir pontes entre culturas, línguas e contextos; é promover consensos sem apagar ou minimizar identidades; é garantir padrões elevados sem impor uniformidade.</p>
<p>Tendo em conta ser determinante que a Confederação reúne Supremos Conselhos, por um lado, Soberanos, isto é, independentes, não se envolvendo nem intervindo em cada um dos seus membros, e, por outro, Regulares, ou seja, afirmando e mantendo, obrigatoriamente, os princípios que lhe estão associados, proponho os seguintes objetivos estratégicos:</p>
<ul>
<li><strong>Coesão pela harmonização</strong>, respeitando a soberania de cada um, de princípios e boas práticas entre os Supremos Conselhos e criando mecanismos transparentes de decisão e prestação de contas.</li>
<li><strong>Formação e aperfeiçoamento</strong>, pela criação e aproveitamento de programas comuns, aproveitando os já existentes de formação de Mestres nos diversos graus, partilhando conteúdos rituais e profanos compatíveis com as nossas tradições, e estimulando a investigação histórica, filosófica e simbólica, com publicações e colóquios internacionais, envolvendo alguns ou a totalidade dos Supremos Conselhos membros.</li>
<li><strong>Solidariedade e impacto social</strong>, através da coordenação de iniciativas de filantropia transnacional em áreas diversas, como por exemplo: educação, saúde, ambiente, mar e ética pública, promovendo civilidade, combate à intolerância e valorização do espaço comum.</li>
<li><strong>Diplomacia fraterna e expansão responsável</strong>, pelo fortalecimento do reconhecimento mútuo entre os nossos Supremos Conselhos regulares, mas também, sem nunca pôr em causa o nosso Regulamento da Confederação, estar aberto ao diálogo com outras organizações maçónicas que trabalhem com o R.E.A.A. e, ainda, acompanhar a expansão para novas regiões com apoio ritual, formativo e ético.</li>
<li><strong>Comunicação e discrição equilibradas mais eficazes</strong>, pela modernização de canais de comunicação institucionais, explicando com serenidade quem somos e o que fazemos, sem ceder ao exibicionismo e com a confidencialidade que resguarda a liberdade interior do trabalho maçónico.</li>
<li><strong>Sustentabilidade e futuro</strong>, através de ferramentas suportadas por digitalização responsável, compreendendo o contributo e as condicionantes da IA, e ativamente preocupados com a continuidade geracional, trazendo Irmãos mais jovens para as nossas iniciativas, lado a lado com a experiência dos mais antigos e, ainda, integrando a dimensão ambiental como expressão do nosso dever para com as gerações vindouras.</li>
</ul>
<p>Nos meus quarenta e oito anos de atividade maçónica ininterrupta, este é mais um projeto que co-iniciei. Sei que, no começo, há sempre muitas propostas, muitas ideias, muito boas intenções e muitas ilusões. Tenho noção clara do risco de se propor para além da capacidade de se concretizar e de poder ser menos bem interpretado mas, sem sonho e ambição, pouco se atingirá e transformará. A minha intenção é de abrir a base da discussão e avaliação coletiva para a consensualização e aprovação das iniciativas a concretizar e continuar a colaborar, daqui a três anos, com o próximo responsável da Confederação, o Soberano Grande Comendador do Supremo Conselho de Marrocos.</p>
<p>Tenho bem consciência da importância para uma organização de uma saudável passagem de testemunho, por maioria de razão quando se trata da primeira transferência de responsabilidade.</p>
<p>Pouco se fará sem o contributo de cada Supremo Conselho, em iniciativas da totalidade dos membros ou agregando parte deles. Peço-vos presença, franqueza e trabalho. Comprometo-me a ouvir antes de decidir, a unir antes de avançar, a servir antes de decidir.</p>
<p>Que a Luz que nos guia inspire a Confederação Internacional dos Supremos Conselhos Soberanos e Regulares. Sigamos juntos, firmes nos valores, claros nos objetivos e fraternos nos gestos, a bem do R.E.A.A., à G.A.D.U.</p>
<p>Nesta época em que vivemos, o ter tem-se sobreposto ao ser e, recentemente, parece que já nem faz falta ter, basta parecer.</p>
<p>Espero que para além de termos uma Confederação, sejamos uma Confederação e, sobretudo, não pareçamos uma Confederação. Dou e darei o meu contributo para que, convosco, sejamos uma Confederação.</p>
""".strip(),
        "placeDate": "Lisboa, 4 de julho de 2026 E∴V∴",
        "signatory": "José Manuel Moreira",
    },
    "en": {
        "salutation": "Most Powerful Sovereign Grand Commanders,<br/>My Illustrious Brethren,",
        "body": """
<p>To uphold and ensure the upholding of the Regulations of the International Confederation of Sovereign and Regular Supreme Councils, today ratified, is the commitment I shall honour and to which I shall contribute so that all honour it.</p>
<p>It is stated therein that the SCP shall hold the first mandate and it is in that capacity that I assume today the presidency of this Confederation. I understand the context in which I received your election. It is therefore with heightened humility and responsibility, a sense of service and the firm conviction that I shall fulfil this mission only by developing consensus and deepening the collective and reciprocal trust initiated and maintained over these past two years, in in-person and virtual meetings, in France, Brazil, Morocco and Portugal.</p>
<p>The strength of Freemasonry rests upon selective recruitment and the personal development of the Mason, thereby contributing to the betterment of Humanity.</p>
<p>The strength of a Supreme Council rests, on the one hand, on the continuous evolution of its members, through the understanding of what Consciousness is — that is, the capacity to perceive oneself and the Context, involving processes that enable attention, self-awareness and the absorption of information by the mind — and, on the other hand, on the strengthening of the spirituality of all, opening portals to states that transcend ordinary reality.</p>
<p>The strength of a Confederation of Supreme Councils rests, notwithstanding the differences in evolutionary stages, size and culture of its members, on the collective capacity to integrate the specific approaches and actions of each one, finding the areas of reflection and the mode of intervention for the building of consensus.</p>
<p>The A.A.S.R., through its Rituals and the Regulations of 1762 and 1786, unites us and provides us with common purposes.</p>
<p>It is in this context that I propose founding values, the guiding thread of our action:</p>
<ul>
<li><strong>Tolerance and respect</strong>, to transform differences of viewpoint into fruitful dialogue.</li>
<li><strong>Fraternity and solidarity</strong>, so that no one is left behind, within and beyond our Supreme Councils.</li>
<li><strong>Integrity and discretion</strong>, because trust is the cement of any lasting work.</li>
<li><strong>The pursuit of Truth and moral improvement</strong>, the silent labour that gives meaning to everything else.</li>
</ul>
<p>Being an international Confederation, these values take on new demands and new opportunities. We need leadership that listens, coordinates and serves. To lead, in this context, is to build bridges between cultures, languages and contexts; it is to promote consensus without erasing or minimizing identities; it is to guarantee high standards without imposing uniformity.</p>
<p>Taking into account that it is essential that the Confederation brings together Supreme Councils that are, on the one hand, Sovereign — that is, independent, neither involving themselves in nor intervening in each of its members — and, on the other hand, Regular — that is, affirming and maintaining, necessarily, the principles associated with them — I propose the following strategic objectives:</p>
<ul>
<li><strong>Cohesion through harmonization</strong>, respecting the sovereignty of each, of principles and good practices among the Supreme Councils, and creating transparent mechanisms of decision-making and accountability.</li>
<li><strong>Education and improvement</strong>, through the creation and development of joint programs, making use of existing ones for the training of Masters at the various degrees, sharing ritual and profane content compatible with our traditions, and stimulating historical, philosophical and symbolic research, with international publications and colloquia involving some or all of the member Supreme Councils.</li>
<li><strong>Solidarity and social impact</strong>, through the coordination of transnational philanthropic initiatives in diverse areas such as education, health, the environment, the sea, and public ethics, promoting civility, the fight against intolerance, and the valorization of the common space.</li>
<li><strong>Fraternal diplomacy and responsible expansion</strong>, by strengthening mutual recognition among our regular Supreme Councils, but also, without ever calling into question our Confederation’s Regulations, being open to dialogue with other Masonic organizations working with the A.A.S.R. and, furthermore, accompanying expansion into new regions with ritual, formative and ethical support.</li>
<li><strong>Balanced and more effective communication and discretion</strong>, through the modernization of institutional communication channels, explaining with serenity who we are and what we do, without yielding to exhibitionism and with the confidentiality that safeguards the inner freedom of Masonic work.</li>
<li><strong>Sustainability and the future</strong>, through tools supported by responsible digitalization, understanding the contribution and constraints of AI, and actively concerned with generational continuity, bringing younger Brethren into our initiatives, side by side with the experience of the more senior, and also integrating the environmental dimension as an expression of our duty towards future generations.</li>
</ul>
<p>In my forty-eight years of uninterrupted Masonic activity, this is yet another project I have co-initiated. I know that, at the outset, there are always many proposals, many ideas, very good intentions and many illusions. I am fully aware of the risk of proposing beyond the capacity to deliver and of being misunderstood, but, without dream and ambition, little will be achieved or transformed. My intention is to open the basis for collective discussion and evaluation for the consensus-building and approval of the initiatives to be implemented, and to continue to collaborate, in three years’ time, with the next head of the Confederation, the Sovereign Grand Commander of the Supreme Council of Morocco.</p>
<p>I am well aware of the importance, for any organization, of a healthy handover, all the more so when it is the first transfer of responsibility.</p>
<p>Little will be accomplished without the contribution of each Supreme Council, in initiatives involving all members or bringing together some of them. I ask of you presence, candor and work. I commit to listening before deciding, to uniting before advancing, to serving before deciding.</p>
<p>May the Light that guides us inspire the International Confederation of Sovereign and Regular Supreme Councils. Let us move forward together, steadfast in our values, clear in our objectives and fraternal in our gestures, for the good of the A.A.S.R., to the G.A.O.T.U.</p>
<p>In the age we live in, <em>having</em> has come to overshadow <em>being</em> and, more recently, it seems that even having no longer seems necessary — it is enough merely to <em>appear</em>.</p>
<p>My hope is that, beyond <em>having</em> a Confederation, we may <em>be</em> a Confederation and, above all, that we do not merely <em>appear</em> to be a Confederation. I give and shall give my contribution so that, together with you, we may <em>be</em> a Confederation.</p>
""".strip(),
        "placeDate": "Lisbon, 4 July 2026 E∴V∴",
        "signatory": "José Manuel Moreira",
    },
    "fr": {
        "salutation": "Très Puissants Souverains Grands Commandeurs,<br/>Mes Illustres Frères,",
        "body": """
<p>Respecter et faire respecter le Règlement de la Confédération Internationale des Suprêmes Conseils Souverains et Réguliers, aujourd’hui ratifié, est l’engagement que je vais honorer et auquel je vais contribuer pour que tous l’honorent.</p>
<p>Il y est stipulé que le SCP aura le premier mandat et c’est en cette qualité que j’assume aujourd’hui la présidence de cette Confédération. Je comprends le contexte dans lequel j’ai reçu votre élection. C’est donc avec humilité et responsabilité accrues, un sens du service et la ferme conviction que je n’accomplirai cette mission qu’en développant des consensus et en approfondissant la confiance collective et réciproque initiée et maintenue au cours de ces deux dernières années, lors de réunions en présentiel et virtuelles, en France, au Brésil, au Maroc et au Portugal.</p>
<p>La force de la Maçonnerie repose sur le recrutement sélectif et le développement personnel du maçon, contribuant ainsi à l’amélioration de l’Humanité.</p>
<p>La force d’un Suprême Conseil repose, d’une part, sur l’évolution continue de ses membres, à travers la compréhension de ce qu’est la Conscience, c’est-à-dire la capacité à se percevoir soi-même et à percevoir le Contexte, impliquant des processus permettant l’attention, la conscience de soi et l’absorption d’informations par l’esprit et, d’autre part, sur le renforcement de la spiritualité de tous, ouvrant des portails vers des états qui transcendent la réalité ordinaire.</p>
<p>La force d’une Confédération de Suprêmes Conseils repose, malgré les différences de stades évolutifs, de dimension et de culture de ses membres, sur la capacité collective d’intégrer les approches et les actions spécifiques de chacun, en trouvant les domaines de réflexion et les modalités d’intervention pour la construction de consensus.</p>
<p>Le R.E.A.A., à travers ses Rituels et les Règlements de 1762 et de 1786, nous rassemble et nous offre des objectifs communs.</p>
<p>C’est dans ce contexte que je propose des valeurs fondatrices, fil conducteur de notre action&nbsp;:</p>
<ul>
<li><strong>Tolérance et respect</strong>, pour transformer les divergences de points de vue en dialogue fécond.</li>
<li><strong>Fraternité et solidarité</strong>, pour que personne ne soit laissé pour compte, au sein et en dehors de nos Suprêmes Conseils.</li>
<li><strong>Intégrité et discrétion</strong>, parce que la confiance est le ciment de toute œuvre durable.</li>
<li><strong>Quête de la Vérité et perfectionnement moral</strong>, le labeur silencieux qui donne sens à tout le reste.</li>
</ul>
<p>En tant que Confédération internationale, ces valeurs acquièrent de nouvelles exigences et de nouvelles opportunités. Nous avons besoin d’un leadership qui écoute, coordonne et serve. Diriger, dans ce cadre, c’est construire des ponts entre les cultures, les langues et les contextes&nbsp;; c’est promouvoir des consensus sans effacer ni minimiser les identités&nbsp;; c’est garantir des standards élevés sans imposer l’uniformité.</p>
<p>Considérant qu’il est essentiel que la Confédération réunisse des Suprêmes Conseils, d’une part, Souverains, c’est-à-dire indépendants, ne s’impliquant ni n’intervenant dans chacun de ses membres, et, d’autre part, Réguliers, c’est-à-dire affirmant et maintenant, obligatoirement, les principes qui leur sont associés, je propose les objectifs stratégiques suivants&nbsp;:</p>
<ul>
<li><strong>Cohésion par l’harmonisation</strong>, en respectant la souveraineté de chacun, des principes et des bonnes pratiques entre les Suprêmes Conseils, et en créant des mécanismes transparents de décision et de reddition de comptes.</li>
<li><strong>Formation et perfectionnement</strong>, par la création et la mise en valeur de programmes communs, en tirant parti des programmes existants de formation des Maîtres aux différents degrés, en partageant des contenus rituels et profanes compatibles avec nos traditions, et en stimulant la recherche historique, philosophique et symbolique, par des publications et des colloques internationaux impliquant certains ou la totalité des Suprêmes Conseils membres.</li>
<li><strong>Solidarité et impact social</strong>, par la coordination d’initiatives de philanthropie transnationale dans divers domaines, tels que l’éducation, la santé, l’environnement, la mer et l’éthique publique, en promouvant la civilité, la lutte contre l’intolérance et la valorisation de l’espace commun.</li>
<li><strong>Diplomatie fraternelle et expansion responsable</strong>, par le renforcement de la reconnaissance mutuelle entre nos Suprêmes Conseils réguliers, mais aussi, sans jamais remettre en cause notre Règlement de la Confédération, en étant ouverts au dialogue avec d’autres organisations maçonniques travaillant avec le R.E.A.A. et, en outre, en accompagnant l’expansion vers de nouvelles régions avec un soutien rituel, formatif et éthique.</li>
<li><strong>Communication et discrétion équilibrées et plus efficaces</strong>, par la modernisation des canaux de communication institutionnels, expliquant avec sérénité qui nous sommes et ce que nous faisons, sans céder à l’exhibitionnisme et avec la confidentialité qui préserve la liberté intérieure du travail maçonnique.</li>
<li><strong>Durabilité et avenir</strong>, grâce à des outils soutenus par une numérisation responsable, en comprenant la contribution et les contraintes de l’IA, et en nous préoccupant activement de la continuité générationnelle, en amenant les Frères plus jeunes à nos initiatives, aux côtés de l’expérience des plus anciens, et en intégrant également la dimension environnementale comme expression de notre devoir envers les générations futures.</li>
</ul>
<p>Au cours de mes quarante-huit années d’activité maçonnique ininterrompue, voici encore un projet que j’ai co-initié. Je sais qu’au début, il y a toujours beaucoup de propositions, beaucoup d’idées, de très bonnes intentions et beaucoup d’illusions. J’ai conscience du risque de proposer au-delà de la capacité à concrétiser et d’être mal interprété, mais, sans rêve et ambition, peu sera atteint et transformé. Mon intention est d’ouvrir la base de la discussion et de l’évaluation collective pour la consensualisation et l’approbation des initiatives à concrétiser, et de continuer à collaborer, dans trois ans, avec le prochain responsable de la Confédération, le Souverain Grand Commandeur du Suprême Conseil du Maroc.</p>
<p>Je suis bien conscient de l’importance, pour une organisation, d’une saine transmission du flambeau, a fortiori lorsqu’il s’agit du premier transfert de responsabilité.</p>
<p>Peu sera accompli sans la contribution de chaque Suprême Conseil, dans des initiatives impliquant la totalité des membres ou une partie d’entre eux. Je vous demande présence, franchise et travail. Je m’engage à écouter avant de décider, à unir avant d’avancer, à servir avant de décider.</p>
<p>Que la Lumière qui nous guide inspire la Confédération Internationale des Suprêmes Conseils Souverains et Réguliers. Avançons ensemble, fermes dans les valeurs, clairs dans les objectifs et fraternels dans les gestes, pour le bien du R.E.A.A., au G.A.D.U.</p>
<p>En cette époque où nous vivons, l’<em>avoir</em> a pris le dessus sur l’<em>être</em> et, récemment, il semble que même l’avoir ne soit plus nécessaire — il suffit de <em>paraître</em>.</p>
<p>J’espère qu’au-delà d’<em>avoir</em> une Confédération, nous <em>soyons</em> une Confédération et, surtout, que nous ne <em>paraissions</em> pas être une Confédération. J’apporte et j’apporterai ma contribution pour que, avec vous, nous <em>soyons</em> une Confédération.</p>
""".strip(),
        "placeDate": "Lisbonne, le 4 juillet 2026 E∴V∴",
        "signatory": "José Manuel Moreira",
    },
}

META = {
    "pt": {
        "communications": {
            "overline": "Comunicações",
            "title": "Comunicações oficiais",
            "lead": "Discursos e comunicações institucionais da Confederação.",
            "speechesHeading": "Discursos",
            "futureNote": "Comunicados e o boletim digital serão publicados nesta área quando disponíveis.",
            "readSpeech": "Ler o discurso",
            "cardDate": "Lisboa · 4 de julho de 2026",
            "cardTitle": "Discurso de posse do Presidente",
            "cardMeta": "José Manuel Moreira · 1.º mandato",
        },
        "speech": {
            "lisboa2026": {
                "overline": "Discurso do Presidente",
                "title": "Discurso de posse",
                "name": "José Manuel Moreira",
                "role": "Presidente da Confederação · Soberano Grande Comendador do Supremo Conselho Português",
                "date": "Lisboa, 4 de julho de 2026",
                "photoAlt": "Retrato de José Manuel Moreira, Presidente da Confederação",
                "pdfHeading": "Descarregar PDF",
                "pdfPt": "Português",
                "pdfEn": "English",
                "pdfFr": "Français",
                "pdfEs": "Español",
                "backComms": "Comunicações",
                "arNote": "",
            }
        },
    },
    "en": {
        "communications": {
            "overline": "Communications",
            "title": "Official communications",
            "lead": "Speeches and institutional communications of the Confederation.",
            "speechesHeading": "Speeches",
            "futureNote": "Statements and the digital bulletin will be published in this area when available.",
            "readSpeech": "Read the address",
            "cardDate": "Lisbon · 4 July 2026",
            "cardTitle": "Presidential inaugural address",
            "cardMeta": "José Manuel Moreira · 1st term",
        },
        "speech": {
            "lisboa2026": {
                "overline": "President’s address",
                "title": "Inaugural address",
                "name": "José Manuel Moreira",
                "role": "President of the Confederation · Sovereign Grand Commander of the Portuguese Supreme Council",
                "date": "Lisbon, 4 July 2026",
                "photoAlt": "Portrait of José Manuel Moreira, President of the Confederation",
                "pdfHeading": "Download PDF",
                "pdfPt": "Português",
                "pdfEn": "English",
                "pdfFr": "Français",
                "pdfEs": "Español",
                "backComms": "Communications",
                "arNote": "",
            }
        },
    },
    "fr": {
        "communications": {
            "overline": "Communications",
            "title": "Communications officielles",
            "lead": "Discours et communications institutionnelles de la Confédération.",
            "speechesHeading": "Discours",
            "futureNote": "Les communiqués et le bulletin numérique seront publiés dans cet espace lorsqu’ils seront disponibles.",
            "readSpeech": "Lire le discours",
            "cardDate": "Lisbonne · 4 juillet 2026",
            "cardTitle": "Discours d’investiture du Président",
            "cardMeta": "José Manuel Moreira · 1er mandat",
        },
        "speech": {
            "lisboa2026": {
                "overline": "Discours du Président",
                "title": "Discours d’investiture",
                "name": "José Manuel Moreira",
                "role": "Président de la Confédération · Souverain Grand Commandeur du Suprême Conseil Portugais",
                "date": "Lisbonne, le 4 juillet 2026",
                "photoAlt": "Portrait de José Manuel Moreira, Président de la Confédération",
                "pdfHeading": "Télécharger le PDF",
                "pdfPt": "Português",
                "pdfEn": "English",
                "pdfFr": "Français",
                "pdfEs": "Español",
                "backComms": "Communications",
                "arNote": "",
            }
        },
    },
    "ar": {
        "communications": {
            "overline": "البيانات",
            "title": "البيانات الرسمية",
            "lead": "خطابات وبيانات مؤسسية للاتحاد.",
            "speechesHeading": "الخطابات",
            "futureNote": "ستُنشر البيانات والنشرة الرقمية في هذا القسم عند توفرها.",
            "readSpeech": "قراءة الخطاب",
            "cardDate": "لشبونة · 4 تموز/يوليو 2026",
            "cardTitle": "خطاب تنصيب الرئيس",
            "cardMeta": "خوسيه مانويل موريرا · الولاية الأولى",
        },
        "speech": {
            "lisboa2026": {
                "overline": "خطاب الرئيس",
                "title": "خطاب التنصيب",
                "name": "خوسيه مانويل موريرا",
                "role": "رئيس الاتحاد · الملك الكبير القائد للمجلس الأعلى البرتغالي",
                "date": "لشبونة، 4 تموز/يوليو 2026",
                "photoAlt": "صورة خوسيه مانويل موريرا، رئيس الاتحاد",
                "pdfHeading": "تنزيل PDF",
                "pdfPt": "Português",
                "pdfEn": "English",
                "pdfFr": "Français",
                "pdfEs": "Español",
                "backComms": "البيانات",
                "arNote": "الترجمة العربية قيد الإعداد. يُعرض أدناه النص الفرنسي؛ يمكن تنزيل الترجمات المتوفرة بصيغة PDF.",
            }
        },
    },
}


def deep_merge(base: dict, patch: dict) -> dict:
    for k, v in patch.items():
        if isinstance(v, dict) and isinstance(base.get(k), dict):
            deep_merge(base[k], v)
        else:
            base[k] = v
    return base


def main() -> None:
    for code in ("pt", "en", "fr", "ar"):
        path = ROOT / "locales" / f"{code}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        patch = META[code]
        speech_src = SPEECH["fr" if code == "ar" else code]
        patch["speech"]["lisboa2026"]["salutation"] = speech_src["salutation"]
        patch["speech"]["lisboa2026"]["bodyHtml"] = speech_src["body"]
        patch["speech"]["lisboa2026"]["placeDate"] = speech_src["placeDate"]
        patch["speech"]["lisboa2026"]["signatory"] = speech_src["signatory"]
        deep_merge(data, patch)
        # Remove obsolete placeholder keys if present
        comm = data.get("communications", {})
        for obsolete in ("willInclude", "b1", "b2", "b3"):
            comm.pop(obsolete, None)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("updated", path.name, "body chars", len(patch["speech"]["lisboa2026"]["bodyHtml"]))


if __name__ == "__main__":
    main()

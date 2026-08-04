# -*- coding: utf-8 -*-
"""Generate multipage HTML site structure (Step 06). Run from repo root."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LOCALE_PATCHES = {
    "pt": {
        "nav": {
            "events": "Eventos",
            "communications": "Comunicações",
            "regulamento": "Regulamento Interno",
        },
        "status": {
            "preparing": "Em preparação",
            "available": "Disponível",
            "emptyMembers": "Nenhum membro adicional publicado",
        },
        "portal": {
            "areasOverline": "Percurso",
            "areasHeading": "Continuar no arquivo institucional.",
            "areasIntro": "As mesmas secções da tradição documental — apresentação, princípios, membros, história e contactos.",
            "teaserMore": "Ler a apresentação completa",
            "pillarsMore": "Ver Declaração de Princípios",
            "membersMore": "Ver jurisdições",
            "contactMore": "Secretariado Internacional",
        },
        "hero": {
            "ctaPrimary": "Conhecer a Confederação",
            "ctaSecondary": "Ver Supremos Conselhos",
        },
        "members": {
            "foundersHeading": "Fundadores",
            "membersHeading": "Membros",
            "membersEmpty": "Além dos Supremos Conselhos fundadores, futuros membros admitidos conforme o Regulamento Interno serão apresentados nesta secção.",
        },
        "communications": {
            "overline": "Comunicações",
            "title": "Comunicações oficiais",
            "lead": "Espaço destinado às comunicações da Confederação, incluindo o Discurso do Presidente.",
            "willInclude": "Virá a incluir:",
            "b1": "Discurso do Presidente",
            "b2": "Comunicados institucionais",
            "b3": "Boletim digital (futuro)",
        },
        "events": {
            "overline": "Agenda",
            "title": "Eventos e reuniões",
            "lead": "Calendário das Assembleias Confederais, encontros institucionais e reuniões relevantes da Confederação.",
            "pastTitle": "Anteriores",
            "pastText": "Os eventos públicos anteriores serão publicados aqui após validação.",
            "upcomingTitle": "Agendadas",
            "upcomingText": "As datas futuras confirmadas serão anunciadas nesta secção.",
        },
        "historyPage": {
            "indexOverline": "História",
            "indexTitle": "Três percursos",
            "indexLead": "A Confederação, os Supremos Conselhos e o R.E.A.A.",
            "confOverline": "História",
            "confTitle": "A Confederação",
            "confBody": "A Confederação Internacional dos Supremos Conselhos Soberanos e Regulares do R.E.A.A. foi criada por tratado assinado em Lyon a 12 de dezembro de 2025 entre o Supremo Conselho do Brasil, o Supremo Conselho para a França, o Supremo Conselho Português e o Supremo Conselho de Marrocos. O Regulamento Interno foi adotado em Lisboa a 3 de julho de 2026. A presidência é rotativa por períodos de três anos entre os membros fundadores, pela ordem: Portugal, Marrocos, Brasil, França.",
            "scOverline": "História",
            "scTitle": "Supremos Conselhos",
            "scLead": "Enquadramento histórico geral da instituição dos Supremos Conselhos no R.E.A.A.",
            "scNote": "Apenas conteúdos validados pela Confederação serão publicados.",
            "reaaOverline": "História",
            "reaaTitle": "Rito Escocês Antigo e Aceite",
            "reaaLead": "Percurso histórico do R.E.A.A. e das leis fundamentais de 1762 e 1786, no respeito pela tradição regular.",
            "reaaNote": "Texto de enquadramento em preparação; ver também Documentos e a Declaração de Princípios.",
            "linkConf": "A Confederação",
            "linkSc": "Supremos Conselhos",
            "linkReaa": "R.E.A.A.",
        },
        "documents": {
            "d1Small": "Declaração",
            "d1Title": "Princípios fundadores",
            "d1Meta": "Texto · Disponível",
            "d2Small": "Regulamento",
            "d2Title": "Regulamento Interno",
            "d2Meta": "PDF · Disponível",
            "d3Small": "1762",
            "d3Title": "Constituições e Regulamentos de 1762",
            "d3Meta": "Consulta histórica · Ligação",
            "d4Small": "1786",
            "d4Title": "Grandes Constituições de 1786",
            "d4Meta": "Consulta histórica · Ligação",
            "regOverline": "Documentos",
            "regTitle": "Regulamento Interno",
            "regLead": "Regulamento Interno da Confederação Internacional dos Supremos Conselhos Soberanos e Regulares do R.E.A.A.",
            "regMeta": "Adotado em Lisboa, 3 de julho de 2026.",
            "regDownload": "Descarregar PDF",
            "c1762Overline": "Documentos fundadores",
            "c1762Title": "Constituições e Regulamentos de 1762",
            "c1762Lead": "Textos fundamentais da Ordem referidos no Regulamento Interno (Art. 2.º) e na Declaração de Princípios.",
            "c1762Disclaimer": "Aviso: as ligações abaixo apontam para edições históricas publicadas no século XIX (domínio público / bibliotecas). Não constituem uma edição oficial da CISCSR; existem várias versões. A Confederação reconhece estes textos como leis fundamentais da Ordem, nos termos do seu Regulamento Interno.",
            "c1762Consult": "Consultar edição histórica",
            "c1762Link1Label": "Internet Archive — Constituições de 1762 (edição breve)",
            "c1762Link2Label": "Internet Archive — Compilação Pike/Macoy 1859 (1762 e 1786)",
            "c1786Overline": "Documentos fundadores",
            "c1786Title": "Grandes Constituições de 1786",
            "c1786Lead": "Textos fundamentais da Ordem referidos no Regulamento Interno (Art. 2.º) e na Declaração de Princípios.",
            "c1786Disclaimer": "Aviso: as ligações abaixo apontam para edições históricas (Gallica / Internet Archive). Não constituem uma edição oficial da CISCSR; a autenticidade histórica do texto de 1786 é discutida pelos historiadores, sem prejuízo do seu reconhecimento institucional pela Confederação.",
            "c1786Consult": "Consultar edição histórica",
            "c1786Link1Label": "Gallica (BnF) — Grandes Constituições de 1786",
            "c1786Link2Label": "Internet Archive — Compilação Pike/Macoy 1859 (1762 e 1786)",
        },
        "page": {
            "backDocs": "Documentos",
            "backHistory": "História",
            "backPrinciples": "Princípios",
            "backHome": "Página inicial",
            "backMembers": "Membros",
        },
    },
    "en": {
        "nav": {
            "events": "Events",
            "communications": "Communications",
            "regulamento": "Internal Regulations",
        },
        "status": {
            "preparing": "In preparation",
            "available": "Available",
            "emptyMembers": "No additional members published",
        },
        "portal": {
            "areasOverline": "Path",
            "areasHeading": "Continue in the institutional archive.",
            "areasIntro": "The same documentary sections — presentation, principles, members, history, and contact.",
            "teaserMore": "Read the full presentation",
            "pillarsMore": "View Declaration of Principles",
            "membersMore": "View jurisdictions",
            "contactMore": "International Secretariat",
        },
        "hero": {
            "ctaPrimary": "Discover the Confederation",
            "ctaSecondary": "View Supreme Councils",
        },
        "members": {
            "foundersHeading": "Founders",
            "membersHeading": "Members",
            "membersEmpty": "In addition to the founding Supreme Councils, future members admitted under the Internal Regulations will be presented in this section.",
        },
        "communications": {
            "overline": "Communications",
            "title": "Official communications",
            "lead": "Space for the Confederation’s communications, including the President’s address.",
            "willInclude": "Will include:",
            "b1": "President’s address",
            "b2": "Institutional communiqués",
            "b3": "Digital bulletin (future)",
        },
        "events": {
            "overline": "Agenda",
            "title": "Events and meetings",
            "lead": "Calendar of Confederate Assemblies, institutional gatherings, and relevant Confederation meetings.",
            "pastTitle": "Past",
            "pastText": "Past public events will be published here after validation.",
            "upcomingTitle": "Upcoming",
            "upcomingText": "Confirmed future dates will be announced in this section.",
        },
        "historyPage": {
            "indexOverline": "History",
            "indexTitle": "Three paths",
            "indexLead": "The Confederation, the Supreme Councils, and the A.A.S.R.",
            "confOverline": "History",
            "confTitle": "The Confederation",
            "confBody": "The International Confederation of Sovereign and Regular Supreme Councils of the A.A.S.R. was created by treaty signed in Lyon on 12 December 2025 between the Supreme Council of Brazil, the Supreme Council for France, the Portuguese Supreme Council, and the Supreme Council of Morocco. The Internal Regulations were adopted in Lisbon on 3 July 2026. The presidency rotates every three years among the founding members, in the order: Portugal, Morocco, Brazil, France.",
            "scOverline": "History",
            "scTitle": "Supreme Councils",
            "scLead": "General historical framing of Supreme Councils within the A.A.S.R.",
            "scNote": "Only content validated by the Confederation will be published.",
            "reaaOverline": "History",
            "reaaTitle": "Ancient and Accepted Scottish Rite",
            "reaaLead": "Historical path of the A.A.S.R. and the fundamental laws of 1762 and 1786, in fidelity to regular tradition.",
            "reaaNote": "Framing text in preparation; see also Documents and the Declaration of Principles.",
            "linkConf": "The Confederation",
            "linkSc": "Supreme Councils",
            "linkReaa": "A.A.S.R.",
        },
        "documents": {
            "d1Small": "Declaration",
            "d1Title": "Founding principles",
            "d1Meta": "Text · Available",
            "d2Small": "Regulations",
            "d2Title": "Internal Regulations",
            "d2Meta": "PDF · Available",
            "d3Small": "1762",
            "d3Title": "Constitutions and Regulations of 1762",
            "d3Meta": "Historical consultation · Link",
            "d4Small": "1786",
            "d4Title": "Grand Constitutions of 1786",
            "d4Meta": "Historical consultation · Link",
            "regOverline": "Documents",
            "regTitle": "Internal Regulations",
            "regLead": "Internal Regulations of the International Confederation of Sovereign and Regular Supreme Councils of the A.A.S.R.",
            "regMeta": "Adopted in Lisbon, 3 July 2026.",
            "regDownload": "Download PDF",
            "c1762Overline": "Founding documents",
            "c1762Title": "Constitutions and Regulations of 1762",
            "c1762Lead": "Fundamental texts of the Order referred to in the Internal Regulations (Art. 2) and the Declaration of Principles.",
            "c1762Disclaimer": "Notice: the links below point to nineteenth-century historical editions (public domain / libraries). They are not an official CISCSR edition; several versions exist. The Confederation recognises these texts as fundamental laws of the Order under its Internal Regulations.",
            "c1762Consult": "Consult a historical edition",
            "c1762Link1Label": "Internet Archive — Constitutions of 1762 (short edition)",
            "c1762Link2Label": "Internet Archive — Pike/Macoy 1859 compilation (1762 and 1786)",
            "c1786Overline": "Founding documents",
            "c1786Title": "Grand Constitutions of 1786",
            "c1786Lead": "Fundamental texts of the Order referred to in the Internal Regulations (Art. 2) and the Declaration of Principles.",
            "c1786Disclaimer": "Notice: the links below point to historical editions (Gallica / Internet Archive). They are not an official CISCSR edition; historians debate the authenticity of the 1786 text, without prejudice to its institutional recognition by the Confederation.",
            "c1786Consult": "Consult a historical edition",
            "c1786Link1Label": "Gallica (BnF) — Grand Constitutions of 1786",
            "c1786Link2Label": "Internet Archive — Pike/Macoy 1859 compilation (1762 and 1786)",
        },
        "page": {
            "backDocs": "Documents",
            "backHistory": "History",
            "backPrinciples": "Principles",
            "backHome": "Home",
            "backMembers": "Members",
        },
    },
    "fr": {
        "nav": {
            "events": "Événements",
            "communications": "Communications",
            "regulamento": "Règlement intérieur",
        },
        "status": {
            "preparing": "En préparation",
            "available": "Disponible",
            "emptyMembers": "Aucun membre supplémentaire publié",
        },
        "portal": {
            "areasOverline": "Parcours",
            "areasHeading": "Poursuivre dans les archives institutionnelles.",
            "areasIntro": "Les mêmes sections documentaires — présentation, principes, membres, histoire et contacts.",
            "teaserMore": "Lire la présentation complète",
            "pillarsMore": "Voir la Déclaration de Principes",
            "membersMore": "Voir les juridictions",
            "contactMore": "Secrétariat international",
        },
        "hero": {
            "ctaPrimary": "Découvrir la Confédération",
            "ctaSecondary": "Voir les Suprêmes Conseils",
        },
        "members": {
            "foundersHeading": "Fondateurs",
            "membersHeading": "Membres",
            "membersEmpty": "Outre les Suprêmes Conseils fondateurs, les futurs membres admis conformément au Règlement intérieur seront présentés dans cette section.",
        },
        "communications": {
            "overline": "Communications",
            "title": "Communications officielles",
            "lead": "Espace destiné aux communications de la Confédération, y compris le Discours du Président.",
            "willInclude": "Comprendra :",
            "b1": "Discours du Président",
            "b2": "Communiqués institutionnels",
            "b3": "Bulletin numérique (futur)",
        },
        "events": {
            "overline": "Agenda",
            "title": "Événements et réunions",
            "lead": "Calendrier des Assemblées confédérales, rencontres institutionnelles et réunions pertinentes de la Confédération.",
            "pastTitle": "Passés",
            "pastText": "Les événements publics passés seront publiés ici après validation.",
            "upcomingTitle": "À venir",
            "upcomingText": "Les dates futures confirmées seront annoncées dans cette section.",
        },
        "historyPage": {
            "indexOverline": "Histoire",
            "indexTitle": "Trois parcours",
            "indexLead": "La Confédération, les Suprêmes Conseils et le R.E.A.A.",
            "confOverline": "Histoire",
            "confTitle": "La Confédération",
            "confBody": "La Confédération internationale des Suprêmes Conseils souverains et réguliers du R.E.A.A. a été créée par traité signé à Lyon le 12 décembre 2025 entre le Suprême Conseil du Brésil, le Suprême Conseil pour la France, le Suprême Conseil Portugais et le Suprême Conseil du Maroc. Le Règlement intérieur a été adopté à Lisbonne le 3 juillet 2026. La présidence est rotative par périodes de trois ans entre les membres fondateurs, dans l’ordre : Portugal, Maroc, Brésil, France.",
            "scOverline": "Histoire",
            "scTitle": "Suprêmes Conseils",
            "scLead": "Cadre historique général de l’institution des Suprêmes Conseils dans le R.E.A.A.",
            "scNote": "Seuls les contenus validés par la Confédération seront publiés.",
            "reaaOverline": "Histoire",
            "reaaTitle": "Rite Écossais Ancien et Accepté",
            "reaaLead": "Parcours historique du R.E.A.A. et des lois fondamentales de 1762 et 1786, dans le respect de la tradition régulière.",
            "reaaNote": "Texte d’encadrement en préparation ; voir aussi Documents et la Déclaration de Principes.",
            "linkConf": "La Confédération",
            "linkSc": "Suprêmes Conseils",
            "linkReaa": "R.E.A.A.",
        },
        "documents": {
            "d1Small": "Déclaration",
            "d1Title": "Principes fondateurs",
            "d1Meta": "Texte · Disponible",
            "d2Small": "Règlement",
            "d2Title": "Règlement intérieur",
            "d2Meta": "PDF · Disponible",
            "d3Small": "1762",
            "d3Title": "Constitutions et Règlements de 1762",
            "d3Meta": "Consultation historique · Lien",
            "d4Small": "1786",
            "d4Title": "Grandes Constitutions de 1786",
            "d4Meta": "Consultation historique · Lien",
            "regOverline": "Documents",
            "regTitle": "Règlement intérieur",
            "regLead": "Règlement intérieur de la Confédération internationale des Suprêmes Conseils souverains et réguliers du R.E.A.A.",
            "regMeta": "Adopté à Lisbonne, le 3 juillet 2026.",
            "regDownload": "Télécharger le PDF",
            "c1762Overline": "Documents fondateurs",
            "c1762Title": "Constitutions et Règlements de 1762",
            "c1762Lead": "Textes fondamentaux de l’Ordre mentionnés dans le Règlement intérieur (art. 2) et la Déclaration de Principes.",
            "c1762Disclaimer": "Avis : les liens ci-dessous renvoient à des éditions historiques du XIXe siècle (domaine public / bibliothèques). Ce ne sont pas une édition officielle de la CISCSR ; plusieurs versions existent. La Confédération reconnaît ces textes comme lois fondamentales de l’Ordre aux termes de son Règlement intérieur.",
            "c1762Consult": "Consulter une édition historique",
            "c1762Link1Label": "Internet Archive — Constitutions de 1762 (édition courte)",
            "c1762Link2Label": "Internet Archive — Compilation Pike/Macoy 1859 (1762 et 1786)",
            "c1786Overline": "Documents fondateurs",
            "c1786Title": "Grandes Constitutions de 1786",
            "c1786Lead": "Textes fondamentaux de l’Ordre mentionnés dans le Règlement intérieur (art. 2) et la Déclaration de Principes.",
            "c1786Disclaimer": "Avis : les liens ci-dessous renvoient à des éditions historiques (Gallica / Internet Archive). Ce ne sont pas une édition officielle de la CISCSR ; l’authenticité historique du texte de 1786 est discutée par les historiens, sans préjudice de sa reconnaissance institutionnelle par la Confédération.",
            "c1786Consult": "Consulter une édition historique",
            "c1786Link1Label": "Gallica (BnF) — Grandes Constitutions de 1786",
            "c1786Link2Label": "Internet Archive — Compilation Pike/Macoy 1859 (1762 et 1786)",
        },
        "page": {
            "backDocs": "Documents",
            "backHistory": "Histoire",
            "backPrinciples": "Principes",
            "backHome": "Accueil",
            "backMembers": "Membres",
        },
    },
    "ar": {
        "nav": {
            "events": "الفعاليات",
            "communications": "البيانات",
            "regulamento": "النظام الداخلي",
        },
        "status": {
            "preparing": "قيد الإعداد",
            "available": "متاح",
            "emptyMembers": "لم يُنشر أي أعضاء إضافيون",
        },
        "portal": {
            "areasOverline": "المسار",
            "areasHeading": "تابع في الأرشيف المؤسسي.",
            "areasIntro": "الأقسام الوثائقية ذاتها — التقديم، المبادئ، الأعضاء، التاريخ، والاتصال.",
            "teaserMore": "قراءة التقديم الكامل",
            "pillarsMore": "عرض إعلان المبادئ",
            "membersMore": "عرض الولايات القضائية",
            "contactMore": "الأمانة الدولية",
        },
        "hero": {
            "ctaPrimary": "التعرّف على الاتحاد",
            "ctaSecondary": "عرض المجالس العليا",
        },
        "members": {
            "foundersHeading": "المؤسسون",
            "membersHeading": "الأعضاء",
            "membersEmpty": "إلى جانب المجالس العليا المؤسسة، سيُعرض في هذا القسم الأعضاء الجدد المقبولون وفق النظام الداخلي.",
        },
        "communications": {
            "overline": "البيانات",
            "title": "بيانات رسمية",
            "lead": "مساحة مخصصة لبيانات الاتحاد، بما في ذلك خطاب الرئيس.",
            "willInclude": "سيشمل:",
            "b1": "خطاب الرئيس",
            "b2": "بيانات مؤسسية",
            "b3": "نشرة رقمية (مستقبلاً)",
        },
        "events": {
            "overline": "الجدول",
            "title": "الفعاليات والاجتماعات",
            "lead": "جدول الجمعيات الاتحادية واللقاءات المؤسسية واجتماعات الاتحاد ذات الصلة.",
            "pastTitle": "السابقة",
            "pastText": "ستُنشر هنا الفعاليات العامة السابقة بعد المصادقة.",
            "upcomingTitle": "القادمة",
            "upcomingText": "ستُعلن في هذا القسم التواريخ المستقبلية المؤكدة.",
        },
        "historyPage": {
            "indexOverline": "التاريخ",
            "indexTitle": "ثلاثة مسارات",
            "indexLead": "الاتحاد، والمجالس العليا، والطقس الإسكتلندي القديم والمقبول.",
            "confOverline": "التاريخ",
            "confTitle": "الاتحاد",
            "confBody": "أُنشئ الاتحاد الدولي للمجالس العليا السيادية والمنتظمة للطقس الإسكتلندي القديم والمقبول بموجب معاهدة وُقّعت في ليون في 12 كانون الأول/ديسمبر 2025 بين المجلس الأعلى للبرازيل والمجلس الأعلى لفرنسا والمجلس الأعلى البرتغالي والمجلس الأعلى للمغرب. واعتُمد النظام الداخلي في لشبونة في 3 تموز/يوليو 2026. والرئاسة دورية لفترات ثلاث سنوات بين الأعضاء المؤسسين بالترتيب: البرتغال، المغرب، البرازيل، فرنسا.",
            "scOverline": "التاريخ",
            "scTitle": "المجالس العليا",
            "scLead": "إطار تاريخي عام لمؤسسة المجالس العليا في الطقس الإسكتلندي القديم والمقبول.",
            "scNote": "لن يُنشر إلا المحتوى الذي يصادق عليه الاتحاد.",
            "reaaOverline": "التاريخ",
            "reaaTitle": "الطقس الإسكتلندي القديم والمقبول",
            "reaaLead": "المسار التاريخي للطقس والقوانين الأساسية لعامي 1762 و1786، في احترام التقليد المنتظم.",
            "reaaNote": "نص تمهيدي قيد الإعداد؛ انظر أيضاً الوثائق وإعلان المبادئ.",
            "linkConf": "الاتحاد",
            "linkSc": "المجالس العليا",
            "linkReaa": "الطقس",
        },
        "documents": {
            "d1Small": "الإعلان",
            "d1Title": "المبادئ المؤسسة",
            "d1Meta": "نص · متاح",
            "d2Small": "النظام",
            "d2Title": "النظام الداخلي",
            "d2Meta": "PDF · متاح",
            "d3Small": "1762",
            "d3Title": "دساتير ولوائح 1762",
            "d3Meta": "مراجعة تاريخية · رابط",
            "d4Small": "1786",
            "d4Title": "الدساتير الكبرى لعام 1786",
            "d4Meta": "مراجعة تاريخية · رابط",
            "regOverline": "الوثائق",
            "regTitle": "النظام الداخلي",
            "regLead": "النظام الداخلي للاتحاد الدولي للمجالس العليا السيادية والمنتظمة للطقس الإسكتلندي القديم والمقبول.",
            "regMeta": "اعتُمد في لشبونة في 3 تموز/يوليو 2026.",
            "regDownload": "تنزيل PDF",
            "c1762Overline": "وثائق مؤسسة",
            "c1762Title": "دساتير ولوائح 1762",
            "c1762Lead": "نصوص أساسية للنظام مذكورة في النظام الداخلي (المادة 2) وفي إعلان المبادئ.",
            "c1762Disclaimer": "تنبيه: الروابط أدناه تشير إلى طبعات تاريخية من القرن التاسع عشر (ملك عام / مكتبات). وهي ليست طبعة رسمية للاتحاد؛ وتوجد عدة نسخ. ويعترف الاتحاد بهذه النصوص قوانين أساسية للنظام وفق نظامه الداخلي.",
            "c1762Consult": "مراجعة طبعة تاريخية",
            "c1762Link1Label": "Internet Archive — دساتير 1762 (طبعة قصيرة)",
            "c1762Link2Label": "Internet Archive — تجميع Pike/Macoy 1859 (1762 و1786)",
            "c1786Overline": "وثائق مؤسسة",
            "c1786Title": "الدساتير الكبرى لعام 1786",
            "c1786Lead": "نصوص أساسية للنظام مذكورة في النظام الداخلي (المادة 2) وفي إعلان المبادئ.",
            "c1786Disclaimer": "تنبيه: الروابط أدناه تشير إلى طبعات تاريخية (Gallica / Internet Archive). وهي ليست طبعة رسمية للاتحاد؛ ويناقش المؤرخون أصالة نص 1786، دون المساس بالاعتراف المؤسسي من الاتحاد.",
            "c1786Consult": "مراجعة طبعة تاريخية",
            "c1786Link1Label": "Gallica (BnF) — الدساتير الكبرى لعام 1786",
            "c1786Link2Label": "Internet Archive — تجميع Pike/Macoy 1859 (1762 و1786)",
        },
        "page": {
            "backDocs": "الوثائق",
            "backHistory": "التاريخ",
            "backPrinciples": "المبادئ",
            "backHome": "الصفحة الأولى",
            "backMembers": "الأعضاء",
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


def patch_locales() -> None:
    for code, patch in LOCALE_PATCHES.items():
        path = ROOT / "locales" / f"{code}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        deep_merge(data, patch)
        # Spelling fix (Latin locales only)
        if code != "ar":
            sigs = data.get("declaration", {}).get("signatories", [])
            for i, s in enumerate(sigs):
                if "El-Fehdi" in s:
                    sigs[i] = s.replace("El-Fehdi", "El Fadhi")
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def head(depth: int, title_fallback: str) -> str:
    p = "../" * depth
    return f"""<!doctype html>
<html lang="pt">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title_fallback}</title>
  <meta name="description" content="Confederação Internacional dos Supremos Conselhos Soberanos e Regulares do Rito Escocês Antigo e Aceite." />
  <link rel="icon" type="image/png" sizes="32x32" href="{p}assets/logo/favicon-32.png" />
  <link rel="apple-touch-icon" href="{p}assets/logo/favicon-180.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@400;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{p}css/styles.css" />
  <link rel="stylesheet" href="{p}css/rtl.css" />
</head>
<body>
  <div class="page-frame">
"""


def header_nav(depth: int, active: str) -> str:
    p = "../" * depth
    home = p if p else "./"
    items = [
        ("confederation", f"{p}confederacao/", "Confederação"),
        ("principles", f"{p}principios/", "Princípios"),
        ("members", f"{p}membros/", "Membros"),
        ("history", f"{p}historia/", "História"),
        ("documents", f"{p}documentos/", "Documentos"),
        ("events", f"{p}eventos/", "Eventos"),
        ("contact", f"{p}contactos/", "Contactos"),
    ]
    links = []
    for key, href, label in items:
        cls = ' class="is-active"' if key == active else ""
        links.append(f'          <a href="{href}"{cls} data-i18n="nav.{key}">{label}</a>')
    return f"""    <header class="site-header">
      <div class="header-inner">
        <a class="brand" href="{home}" data-i18n-attr="aria-label:nav.home">
          <img class="brand-logo" src="{p}assets/logo/logo-header.png" width="50" height="50" alt="" data-i18n-attr="alt:meta.logoAlt" />
          <span class="brand-copy">
            <strong data-i18n="brand.short">Confederação Internacional</strong>
            <small data-i18n="brand.long" data-i18n-html>Supremos Conselhos Soberanos e Regulares<br/>do R.E.A.A.</small>
          </span>
        </a>
        <div class="header-tools">
          <div class="lang-switcher" role="group" aria-label="Language"></div>
          <button class="menu-button" type="button" data-i18n="nav.menu">Menu</button>
        </div>
        <nav class="main-nav" data-i18n-attr="aria-label:nav.main">
{chr(10).join(links)}
        </nav>
      </div>
    </header>
"""


def motto_band() -> str:
    return """      <section class="motto">
        <p data-i18n="motto">“Cooperação, regularidade e soberania em fidelidade à tradição.”</p>
      </section>
"""


def page_banner(overline_key: str, overline_fb: str, title_key: str, title_fb: str, html_title: bool = False) -> str:
    html_attr = ' data-i18n-html' if html_title else ""
    return f"""      <section class="page-banner">
        <div class="ornament ornament-top" aria-hidden="true"></div>
        <p class="overline" data-i18n="{overline_key}">{overline_fb}</p>
        <h1 data-i18n="{title_key}"{html_attr}>{title_fb}</h1>
        <div class="ornament ornament-bottom" aria-hidden="true"></div>
      </section>
"""


def footer(depth: int, with_motto: bool = True) -> str:
    p = "../" * depth
    motto = motto_band() if with_motto else ""
    return f"""{motto}    <footer class="site-footer">
      <nav class="footer-nav" aria-label="Secondary">
        <a href="{p}comunicacoes/" data-i18n="nav.communications">Comunicações</a>
        <a href="{p}principios/#declaracao" data-i18n="nav.declaration">Declaração</a>
        <a href="{p}documentos/regulamento-interno/" data-i18n="nav.regulamento">Regulamento Interno</a>
      </nav>
      <p>
        <strong data-i18n="footer.name">Confederação Internacional dos Supremos Conselhos Soberanos e Regulares do R.E.A.A.</strong>
      </p>
      <p data-i18n="footer.copy">© 2026 · CISCSR</p>
    </footer>
  </div>
  <script src="{p}js/i18n.js"></script>
  <script src="{p}js/main.js"></script>
</body>
</html>
"""


def write(rel: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", rel)


def status_block(extra_html: str = "") -> str:
    return f"""        <aside class="status-block" aria-live="polite">
          <p class="status-label" data-i18n="status.preparing">Em preparação</p>
{extra_html}        </aside>
"""


def page_actions(links: list[tuple[str, str, str]]) -> str:
    parts = []
    for href, key, fallback in links:
        parts.append(f'<a href="{href}" data-i18n="{key}">{fallback}</a>')
    return f'        <p class="page-actions">{" · ".join(parts)}</p>\n'


def build() -> None:
    patch_locales()

    # Brochure-style home (multipage links, original rhythm)
    write(
        "index.html",
        head(0, "CISCSR")
        + header_nav(0, "")
        + """    <main>
      <section class="hero">
        <div class="ornament ornament-top" aria-hidden="true"></div>
        <p class="overline" data-i18n="hero.overline">Soberania · Regularidade · Cooperação</p>
        <div class="hero-logo-wrap">
          <img class="hero-logo" src="assets/logo/logo-hero.png" width="118" height="118" alt="" data-i18n-attr="alt:meta.logoAlt" />
        </div>
        <h1>
          <span data-i18n="hero.title" data-i18n-html>Confederação Internacional dos Supremos Conselhos<br/>Soberanos e Regulares</span>
          <span data-i18n="hero.titleSpan">do Rito Escocês Antigo e Aceite</span>
        </h1>
        <p class="hero-text" data-i18n="hero.text">Instituição confederal dedicada à cooperação fraterna entre Supremos Conselhos, no respeito pela soberania jurisdicional e à preservação da tradição regular do R.E.A.A.</p>
        <div class="hero-actions">
          <a class="button button-primary" href="confederacao/" data-i18n="hero.ctaPrimary">Conhecer a Confederação</a>
          <a class="button button-secondary" href="membros/" data-i18n="hero.ctaSecondary">Ver Supremos Conselhos</a>
        </div>
        <div class="ornament ornament-bottom" aria-hidden="true"></div>
      </section>

      <section class="section section-light">
        <div class="section-title">
          <p class="overline" data-i18n="confederation.overline">Confederação</p>
          <h2 data-i18n="confederation.heading" data-i18n-html>Unir sem absorver.<br/>Representar sem substituir.</h2>
        </div>
        <div class="two-columns">
          <p class="lead" data-i18n="confederation.lead"></p>
          <div class="text-block">
            <p data-i18n="confederation.p1"></p>
            <p><a class="text-link" href="confederacao/" data-i18n="portal.teaserMore">Ler a apresentação completa</a></p>
          </div>
        </div>
      </section>

      <section class="section section-warm">
        <div class="section-title centered">
          <p class="overline" data-i18n="pillars.overline">Princípios fundadores</p>
          <h2 data-i18n="pillars.heading">Quatro pilares de uma ordem confederal.</h2>
        </div>
        <div class="principles">
          <article><span>I</span><h3 data-i18n="pillars.oneTitle">Regularidade</h3><p data-i18n="pillars.oneText"></p></article>
          <article><span>II</span><h3 data-i18n="pillars.twoTitle">Soberania</h3><p data-i18n="pillars.twoText"></p></article>
          <article><span>III</span><h3 data-i18n="pillars.threeTitle">Fraternidade</h3><p data-i18n="pillars.threeText"></p></article>
          <article><span>IV</span><h3 data-i18n="pillars.fourTitle">Continuidade</h3><p data-i18n="pillars.fourText"></p></article>
        </div>
        <p class="centered-action"><a class="button button-primary button-on-light" href="principios/#declaracao" data-i18n="portal.pillarsMore">Ver Declaração de Princípios</a></p>
      </section>

      <section class="section section-dark">
        <div class="section-title centered">
          <p class="overline" data-i18n="members.overline">Supremos Conselhos Membros</p>
          <h2 data-i18n="members.heading">Jurisdições soberanas em cooperação internacional.</h2>
        </div>
        <div class="member-panel">
          <div class="member-map" data-i18n-attr="aria-label:members.mapLabel">
            <img class="member-map-svg" src="assets/map/world.svg?v=3" width="1000" height="500" alt="" />
          </div>
          <div class="member-table" data-i18n-members="members.items"></div>
        </div>
        <p class="centered-action"><a class="button button-secondary" href="membros/" data-i18n="portal.membersMore">Ver jurisdições</a></p>
      </section>

      <section class="section section-light">
        <div class="section-title">
          <p class="overline" data-i18n="history.overline">História e enquadramento</p>
          <h2 data-i18n="history.heading">Uma tradição antiga com vocação internacional.</h2>
        </div>
        <div class="chronology">
          <article>
            <time data-i18n="history.t1">1761–1801</time>
            <div>
              <h3 data-i18n="history.t1Title">Formação histórica</h3>
              <p data-i18n="history.t1Text"></p>
            </div>
          </article>
          <article>
            <time data-i18n="history.t2">Séc. XIX–XX</time>
            <div>
              <h3 data-i18n="history.t2Title">Expansão das jurisdições</h3>
              <p data-i18n="history.t2Text"></p>
            </div>
          </article>
          <article>
            <time data-i18n="history.t3">2025–2026</time>
            <div>
              <h3 data-i18n="history.t3Title">Fundação da Confederação</h3>
              <p data-i18n="history.t3Text"></p>
            </div>
          </article>
        </div>
        <p class="centered-action"><a class="text-link" href="historia/" data-i18n="nav.history">História</a></p>
      </section>

      <section class="section section-warm">
        <div class="section-title centered">
          <p class="overline" data-i18n="documents.overline">Documentos públicos</p>
          <h2 data-i18n="documents.heading">Arquivo institucional.</h2>
        </div>
        <div class="documents documents-4">
          <a href="principios/#declaracao">
            <small data-i18n="documents.d1Small">Declaração</small>
            <strong data-i18n="documents.d1Title">Princípios fundadores</strong>
            <span data-i18n="documents.d1Meta">Texto · Disponível</span>
          </a>
          <a href="documentos/regulamento-interno/">
            <small data-i18n="documents.d2Small">Regulamento</small>
            <strong data-i18n="documents.d2Title">Regulamento Interno</strong>
            <span data-i18n="documents.d2Meta">PDF · Disponível</span>
          </a>
          <a href="documentos/1762/">
            <small data-i18n="documents.d3Small">1762</small>
            <strong data-i18n="documents.d3Title">Constituições e Regulamentos de 1762</strong>
            <span data-i18n="documents.d3Meta">Em preparação</span>
          </a>
          <a href="documentos/1786/">
            <small data-i18n="documents.d4Small">1786</small>
            <strong data-i18n="documents.d4Title">Grandes Constituições de 1786</strong>
            <span data-i18n="documents.d4Meta">Em preparação</span>
          </a>
        </div>
      </section>

      <section class="section section-light">
        <div class="section-title centered">
          <p class="overline" data-i18n="portal.areasOverline">Percurso</p>
          <h2 data-i18n="portal.areasHeading">Continuar no arquivo institucional.</h2>
          <p class="section-intro" data-i18n="portal.areasIntro"></p>
        </div>
        <div class="documents">
          <a href="eventos/">
            <small data-i18n="nav.events">Eventos</small>
            <strong data-i18n="events.title">Eventos e reuniões</strong>
            <span data-i18n="status.preparing">Em preparação</span>
          </a>
          <a href="comunicacoes/">
            <small data-i18n="nav.communications">Comunicações</small>
            <strong data-i18n="communications.title">Comunicações oficiais</strong>
            <span data-i18n="status.preparing">Em preparação</span>
          </a>
          <a href="contactos/">
            <small data-i18n="nav.contact">Contactos</small>
            <strong data-i18n="contact.heading">Secretariado Internacional</strong>
            <span data-i18n="status.available">Disponível</span>
          </a>
        </div>
      </section>
    </main>
"""
        + footer(0),
    )

    # Confederacao
    write(
        "confederacao/index.html",
        head(1, "Confederação — CISCSR")
        + header_nav(1, "confederation")
        + """    <main>
"""
        + page_banner("confederation.overline", "Confederação", "confederation.heading", "Unir sem absorver.<br/>Representar sem substituir.", True)
        + """      <section class="section section-light">
        <div class="two-columns">
          <p class="lead" data-i18n="confederation.lead"></p>
          <div class="text-block">
            <p data-i18n="confederation.p1"></p>
            <p data-i18n="confederation.p2"></p>
            <p data-i18n="confederation.p3"></p>
          </div>
        </div>
      </section>
    </main>
"""
        + footer(1),
    )

    # Principios
    write(
        "principios/index.html",
        head(1, "Princípios — CISCSR")
        + header_nav(1, "principles")
        + """    <main>
"""
        + page_banner("pillars.overline", "Princípios fundadores", "pillars.heading", "Quatro pilares de uma ordem confederal.")
        + """      <section class="section section-warm">
        <div class="principles">
          <article><span>I</span><h3 data-i18n="pillars.oneTitle">Regularidade</h3><p data-i18n="pillars.oneText"></p></article>
          <article><span>II</span><h3 data-i18n="pillars.twoTitle">Soberania</h3><p data-i18n="pillars.twoText"></p></article>
          <article><span>III</span><h3 data-i18n="pillars.threeTitle">Fraternidade</h3><p data-i18n="pillars.threeText"></p></article>
          <article><span>IV</span><h3 data-i18n="pillars.fourTitle">Continuidade</h3><p data-i18n="pillars.fourText"></p></article>
        </div>
        <div id="declaracao" class="declaration">
          <div class="section-title">
            <p class="overline" data-i18n="declaration.overline">Documento oficial</p>
            <h2 data-i18n="declaration.heading">Declaração de Princípios</h2>
          </div>
          <p class="declaration-intro" data-i18n="declaration.intro"></p>
          <div class="declaration-block"><h3 data-i18n="declaration.proclaimsHeading">Proclama:</h3><ul data-i18n-list="declaration.proclaims"></ul></div>
          <div class="declaration-block"><h3 data-i18n="declaration.recallsHeading">Recorda:</h3><ul data-i18n-list="declaration.recalls"></ul></div>
          <div class="declaration-block"><h3 data-i18n="declaration.attachedHeading">Está vinculada:</h3><ul data-i18n-list="declaration.attached"></ul></div>
          <div class="declaration-block"><h3 data-i18n="declaration.commitsHeading">Compromete-se a:</h3><ul data-i18n-list="declaration.commits"></ul></div>
          <div class="declaration-signatories" data-i18n-signatories="declaration.signatories"></div>
        </div>
      </section>
    </main>
"""
        + footer(1),
    )

    # Membros
    write(
        "membros/index.html",
        head(1, "Membros — CISCSR")
        + header_nav(1, "members")
        + """    <main>
"""
        + page_banner("members.overline", "Supremos Conselhos Membros", "members.heading", "Jurisdições soberanas em cooperação internacional.")
        + """      <section class="section section-dark">
        <div class="member-panel">
          <div class="member-map" data-i18n-attr="aria-label:members.mapLabel">
            <img class="member-map-svg" src="../assets/map/world.svg?v=3" width="1000" height="500" alt="" />
          </div>
          <div>
            <h2 class="members-subhead" data-i18n="members.foundersHeading">Fundadores</h2>
            <div class="member-table" data-i18n-members="members.items"></div>
          </div>
        </div>
      </section>
      <section class="section section-light">
        <div class="section-title">
          <h2 data-i18n="members.membersHeading">Membros</h2>
        </div>
        <aside class="status-block status-block-empty">
          <p data-i18n="members.membersEmpty"></p>
          <p class="status-label" data-i18n="status.emptyMembers">Nenhum membro adicional publicado</p>
        </aside>
      </section>
    </main>
"""
        + footer(1),
    )

    # Historia index
    write(
        "historia/index.html",
        head(1, "História — CISCSR")
        + header_nav(1, "history")
        + """    <main>
"""
        + page_banner("historyPage.indexOverline", "História", "historyPage.indexTitle", "Três percursos")
        + """      <section class="section section-light">
        <p class="lead" data-i18n="historyPage.indexLead"></p>
        <div class="documents">
          <a href="confederacao/">
            <small data-i18n="historyPage.indexOverline">História</small>
            <strong data-i18n="historyPage.linkConf">A Confederação</strong>
            <span data-i18n="status.available">Disponível</span>
          </a>
          <a href="supremos-conselhos/">
            <small data-i18n="historyPage.indexOverline">História</small>
            <strong data-i18n="historyPage.linkSc">Supremos Conselhos</strong>
            <span data-i18n="status.preparing">Em preparação</span>
          </a>
          <a href="reaa/">
            <small data-i18n="historyPage.indexOverline">História</small>
            <strong data-i18n="historyPage.linkReaa">R.E.A.A.</strong>
            <span data-i18n="status.preparing">Em preparação</span>
          </a>
        </div>
      </section>
    </main>
"""
        + footer(1),
    )

    write(
        "historia/confederacao/index.html",
        head(2, "História · Confederação — CISCSR")
        + header_nav(2, "history")
        + """    <main>
"""
        + page_banner("historyPage.confOverline", "História", "historyPage.confTitle", "A Confederação")
        + """      <section class="section section-light">
        <p class="lead" data-i18n="historyPage.confBody"></p>
"""
        + page_actions([("../../historia/", "page.backHistory", "História"), ("../../", "page.backHome", "Página inicial")])
        + """      </section>
    </main>
"""
        + footer(2),
    )

    for slug, title_key, lead_key, note_key, title_fb in [
        ("supremos-conselhos", "historyPage.scTitle", "historyPage.scLead", "historyPage.scNote", "Supremos Conselhos"),
        ("reaa", "historyPage.reaaTitle", "historyPage.reaaLead", "historyPage.reaaNote", "R.E.A.A."),
    ]:
        over = "historyPage.scOverline" if slug != "reaa" else "historyPage.reaaOverline"
        write(
            f"historia/{slug}/index.html",
            head(2, f"História · {title_fb} — CISCSR")
            + header_nav(2, "history")
            + f"""    <main>
"""
            + page_banner(over, "História", title_key, title_fb)
            + f"""      <section class="section section-light">
        <p class="lead" data-i18n="{lead_key}"></p>
"""
            + status_block(f'          <p data-i18n="{note_key}"></p>\n')
            + page_actions(
                [
                    ("../../historia/", "page.backHistory", "História"),
                    ("../../documentos/", "page.backDocs", "Documentos"),
                    ("../../", "page.backHome", "Página inicial"),
                ]
            )
            + """      </section>
    </main>
"""
            + footer(2),
        )

    # Documentos
    write(
        "documentos/index.html",
        head(1, "Documentos — CISCSR")
        + header_nav(1, "documents")
        + """    <main>
"""
        + page_banner("documents.overline", "Documentos públicos", "documents.heading", "Arquivo institucional.")
        + """      <section class="section section-warm">
        <div class="documents documents-4">
          <a href="../principios/#declaracao">
            <small data-i18n="documents.d1Small">Declaração</small>
            <strong data-i18n="documents.d1Title">Princípios fundadores</strong>
            <span data-i18n="documents.d1Meta">Texto · Disponível</span>
          </a>
          <a href="regulamento-interno/">
            <small data-i18n="documents.d2Small">Regulamento</small>
            <strong data-i18n="documents.d2Title">Regulamento Interno</strong>
            <span data-i18n="documents.d2Meta">PDF · Disponível</span>
          </a>
          <a href="1762/">
            <small data-i18n="documents.d3Small">1762</small>
            <strong data-i18n="documents.d3Title">Constituições e Regulamentos de 1762</strong>
            <span data-i18n="documents.d3Meta">Em preparação</span>
          </a>
          <a href="1786/">
            <small data-i18n="documents.d4Small">1786</small>
            <strong data-i18n="documents.d4Title">Grandes Constituições de 1786</strong>
            <span data-i18n="documents.d4Meta">Em preparação</span>
          </a>
        </div>
      </section>
    </main>
"""
        + footer(1),
    )

    write(
        "documentos/regulamento-interno/index.html",
        head(2, "Regulamento Interno — CISCSR")
        + header_nav(2, "documents")
        + """    <main>
"""
        + page_banner("documents.regOverline", "Documentos", "documents.regTitle", "Regulamento Interno")
        + """      <section class="section section-warm">
        <p class="lead" data-i18n="documents.regLead"></p>
        <p data-i18n="documents.regMeta"></p>
        <p class="page-actions">
          <a class="button button-primary button-on-light" href="../../Docs/Regulamento-Interno-CISCSR.pdf" target="_blank" rel="noopener" data-i18n="documents.regDownload">Descarregar PDF</a>
        </p>
"""
        + page_actions([("../", "page.backDocs", "Documentos"), ("../../", "page.backHome", "Página inicial")])
        + """      </section>
    </main>
"""
        + footer(2),
    )

    # 1762 / 1786 — historical consultation links (not CISCSR-official editions)
    write(
        "documentos/1762/index.html",
        head(2, "Constituições 1762 — CISCSR")
        + header_nav(2, "documents")
        + """    <main>
"""
        + page_banner("documents.c1762Overline", "Documentos fundadores", "documents.c1762Title", "Constituições e Regulamentos de 1762")
        + """      <section class="section section-warm">
        <p class="lead" data-i18n="documents.c1762Lead"></p>
        <aside class="status-block disclaimer-block">
          <p class="status-label" data-i18n="documents.c1762Consult">Consultar edição histórica</p>
          <p data-i18n="documents.c1762Disclaimer"></p>
          <ul class="external-links">
            <li>
              <a href="https://archive.org/details/constitutionsreg00scot" target="_blank" rel="noopener noreferrer" data-i18n="documents.c1762Link1Label">Internet Archive — Constituições de 1762 (edição breve)</a>
            </li>
            <li>
              <a href="https://archive.org/details/statutesregulati00free" target="_blank" rel="noopener noreferrer" data-i18n="documents.c1762Link2Label">Internet Archive — Compilação Pike/Macoy 1859 (1762 e 1786)</a>
            </li>
          </ul>
        </aside>
"""
        + page_actions(
            [
                ("../", "page.backDocs", "Documentos"),
                ("../../principios/", "page.backPrinciples", "Princípios"),
                ("../../", "page.backHome", "Página inicial"),
            ]
        )
        + """      </section>
    </main>
"""
        + footer(2),
    )

    write(
        "documentos/1786/index.html",
        head(2, "Constituições 1786 — CISCSR")
        + header_nav(2, "documents")
        + """    <main>
"""
        + page_banner("documents.c1786Overline", "Documentos fundadores", "documents.c1786Title", "Grandes Constituições de 1786")
        + """      <section class="section section-warm">
        <p class="lead" data-i18n="documents.c1786Lead"></p>
        <aside class="status-block disclaimer-block">
          <p class="status-label" data-i18n="documents.c1786Consult">Consultar edição histórica</p>
          <p data-i18n="documents.c1786Disclaimer"></p>
          <ul class="external-links">
            <li>
              <a href="https://gallica.bnf.fr/ark:/12148/bpt6k329509h" target="_blank" rel="noopener noreferrer" data-i18n="documents.c1786Link1Label">Gallica (BnF) — Grandes Constituições de 1786</a>
            </li>
            <li>
              <a href="https://archive.org/details/statutesregulati00free" target="_blank" rel="noopener noreferrer" data-i18n="documents.c1786Link2Label">Internet Archive — Compilação Pike/Macoy 1859 (1762 e 1786)</a>
            </li>
          </ul>
        </aside>
"""
        + page_actions(
            [
                ("../", "page.backDocs", "Documentos"),
                ("../../principios/", "page.backPrinciples", "Princípios"),
                ("../../", "page.backHome", "Página inicial"),
            ]
        )
        + """      </section>
    </main>
"""
        + footer(2),
    )

    write(
        "eventos/index.html",
        head(1, "Eventos — CISCSR")
        + header_nav(1, "events")
        + """    <main>
"""
        + page_banner("events.overline", "Agenda", "events.title", "Eventos e reuniões")
        + """      <section class="section section-light">
        <p class="lead" data-i18n="events.lead"></p>
"""
        + status_block(
            """          <div class="event-blocks">
            <div>
              <h2 data-i18n="events.pastTitle">Anteriores</h2>
              <p data-i18n="events.pastText"></p>
            </div>
            <div>
              <h2 data-i18n="events.upcomingTitle">Agendadas</h2>
              <p data-i18n="events.upcomingText"></p>
            </div>
          </div>
"""
        )
        + page_actions(
            [
                ("../historia/", "page.backHistory", "História"),
                ("../contactos/", "nav.contact", "Contactos"),
                ("../", "page.backHome", "Página inicial"),
            ]
        )
        + """      </section>
    </main>
"""
        + footer(1),
    )

    write(
        "comunicacoes/index.html",
        head(1, "Comunicações — CISCSR")
        + header_nav(1, "communications")
        + """    <main>
"""
        + page_banner("communications.overline", "Comunicações", "communications.title", "Comunicações oficiais")
        + """      <section class="section section-light">
        <p class="lead" data-i18n="communications.lead"></p>
"""
        + status_block(
            """          <p data-i18n="communications.willInclude">Virá a incluir:</p>
          <ul>
            <li data-i18n="communications.b1">Discurso do Presidente</li>
            <li data-i18n="communications.b2">Comunicados institucionais</li>
            <li data-i18n="communications.b3">Boletim digital (futuro)</li>
          </ul>
"""
        )
        + page_actions([("../contactos/", "nav.contact", "Contactos"), ("../", "page.backHome", "Página inicial")])
        + """      </section>
    </main>
"""
        + footer(1),
    )

    write(
        "contactos/index.html",
        head(1, "Contactos — CISCSR")
        + header_nav(1, "contact")
        + """    <main>
"""
        + page_banner("contact.overline", "Contactos", "contact.heading", "Secretariado Internacional")
        + """      <section class="section section-light contact">
        <p class="section-intro" data-i18n="contact.intro"></p>
        <form class="contact-form">
          <label>
            <span data-i18n="contact.name">Nome</span>
            <input type="text" data-i18n-attr="placeholder:contact.namePlaceholder" placeholder="Nome completo" />
          </label>
          <label>
            <span data-i18n="contact.email">Email</span>
            <input type="email" data-i18n-attr="placeholder:contact.emailPlaceholder" placeholder="email@exemplo.org" />
          </label>
          <label>
            <span data-i18n="contact.message">Mensagem</span>
            <textarea rows="5" data-i18n-attr="placeholder:contact.messagePlaceholder" placeholder="Escreva a sua mensagem"></textarea>
          </label>
          <button class="button button-primary button-on-light" type="button" data-i18n="contact.submit">Enviar pedido</button>
        </form>
      </section>
    </main>
"""
        + footer(1),
    )

    print("done")


if __name__ == "__main__":
    build()

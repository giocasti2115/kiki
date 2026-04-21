from __future__ import annotations

"""Utility to sync favicon references and inject curated internal layouts."""

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
from typing import Dict, List, Sequence

ROOT = Path(__file__).resolve().parents[1]
HTML_GLOB = "*.html"
PRESERVE_LAYOUT = {"index.html", "index-2.html", "who-is-it.html", "team.html", "services.html"}
FAVICON_OLD = "assets/images/favicon.png"
FAVICON_NEW = "assets/images/logo/logo-sonrisa_16x16.svg"

PREFIX_TITLE_MAP = {
    "solucion-": "Solución",
    "servicio-": "Servicio",
    "caso-": "Caso",
    "casos-": "Casos",
    "capacidad-": "Capacidad",
    "cobertura-": "Cobertura",
    "perfil-": "Perfil",
    "recurso-": "Recurso",
}

EXPLICIT_TITLES = {
    "about": "Sobre Kiki",
    "blog": "Blog Kiki Latam",
    "career": "Carreras en Kiki",
    "contact-us": "Contacto",
    "coverage": "Cobertura Kiki",
    "faq": "Preguntas Frecuentes",
    "pricing-plan": "Planes y Tarifas",
    "services-2": "Casos por tipo de cliente",
    "services-3": "Testimonios y métricas",
    "solutions": "Soluciones Kiki",
    "services": "Servicios Kiki",
    "team": "Equipo Kiki",
    "who-is-it": "Para quién es Kiki",
}

EXPLICIT_DESCRIPTIONS = {
    "coverage": "Resumen de presencia geográfica y capacidades regionales.",
    "blog": "Componentes editoriales para artículos, recursos y anuncios.",
    "career": "Sección para presentar vacantes, cultura y beneficios.",
    "contact-us": "Formulario base para leads comerciales o soporte.",
    "pricing-plan": "Comparativa de paquetes, SLAs y add-ons.",
    "faq": "Base para preguntas frecuentes y respuestas rápidas.",
}

EXPLICIT_TEMPLATE = {
    "about": "who",
    "blog": "services",
    "career": "team",
    "contact-us": "services",
    "coverage": "who",
    "faq": "who",
    "pricing-plan": "services",
    "solutions": "services",
    "services-2": "team",
    "services-3": "team",
}

TEAM_LIKE_PREFIXES = ("caso-", "casos-")
SERVICE_LIKE_PREFIXES = ("servicio-", "solucion-")
INFO_LIKE_PREFIXES = ("capacidad-", "cobertura-", "perfil-", "recurso-")

TEAM_IMAGES = [
    "assets/images/our_team/01.jpg",
    "assets/images/our_team/02.jpg",
    "assets/images/our_team/04.jpg",
    "assets/images/our_team/05.jpg",
]

SERVICE_ICONS = [
    "assets/images/icon/icon-1.png",
    "assets/images/icon/icon-2.png",
    "assets/images/icon/icon-3.png",
    "assets/images/icon/icon-4.png",
    "assets/images/icon/icon-5.png",
    "assets/images/icon/icon-6.png",
]

STAT_ICONS = [
    "assets/images/icon/count-1.png",
    "assets/images/icon/count-2.png",
    "assets/images/icon/count-3.png",
    "assets/images/icon/count-4.png",
]

@dataclass
class PageMeta:
    slug: str
    title: str
    description: str
    breadcrumb: str
    tagline: str
    highlight_intro: str
    highlight_span: str
    stats: Sequence[Dict[str, str]]
    skills: Sequence[Dict[str, str]]
    stories: Sequence[Dict[str, str]]
    features: Sequence[Dict[str, str]]
    breadcrumb_class: str = ""


def slug_to_title(slug: str) -> str:
    if slug in EXPLICIT_TITLES:
        return EXPLICIT_TITLES[slug]
    for prefix, label in PREFIX_TITLE_MAP.items():
        if slug.startswith(prefix):
            remainder = slug[len(prefix):].replace("-", " ").strip()
            if remainder:
                remainder = remainder.title()
            return f"{label} {remainder}".strip()
    return slug.replace("-", " ").title()


def make_description(slug: str, title: str) -> str:
    base = EXPLICIT_DESCRIPTIONS.get(slug)
    if base:
        return base
    return f"Plantilla base para {title.lower()}. Actualiza este texto con el contenido definitivo."


def default_stats() -> List[Dict[str, str]]:
    return [
        {"start": "0", "end": "1200", "suffix": "+", "label": "Clientes activos"},
        {"start": "0", "end": "250", "suffix": "+", "label": "Lanzamientos anuales"},
        {"start": "0", "end": "18", "suffix": "+", "label": "Países cubiertos"},
        {"start": "0", "end": "72", "suffix": "h", "label": "Ventana SLA típica"},
    ]


def default_skills() -> List[Dict[str, str]]:
    return [
        {"label": "Arquitectura Comercial", "class": "bar-1"},
        {"label": "Operación Logística", "class": "bar-2"},
        {"label": "Pagos & Risk", "class": "bar-3"},
        {"label": "Éxito del Cliente", "class": "bar-4"},
    ]


def default_stories(title: str) -> List[Dict[str, str]]:
    stories = []
    blueprints = [
        ("Playbook de entrada", "Mapea retos y quick wins para {title}."),
        ("Orquestación diaria", "Define pods compartidos para que {title} escale sin fricción."),
        ("Gobernanza & métricas", "Alinea KPIs de {title} con promesas comerciales."),
        ("Éxito ampliado", "Expande el alcance de {title} con casos espejo."),
    ]
    for idx, (heading, blurb) in enumerate(blueprints):
        stories.append(
            {
                "heading": f"{heading}",
                "role": f"Módulo 0{idx + 1}",
                "description": blurb.format(title=title.lower()),
                "secondary": "Sustituye este copy por el detalle de la historia real del cliente.",
                "cta": "Hablar con Kiki",
                "image": TEAM_IMAGES[idx % len(TEAM_IMAGES)],
                "cta_link": "contact-us.html",
            }
        )
    return stories


def default_features(title: str) -> List[Dict[str, str]]:
    tags = [
        "Descubrimiento",
        "Arquitectura",
        "Implementación",
        "Pagos locales",
        "Operación diaria",
        "Inteligencia",
    ]
    features = []
    for idx, tag in enumerate(tags):
        features.append(
            {
                "title": f"{tag}",
                "copy": f"Placeholder para describir el módulo '{tag}' enfocado en {title.lower()}.",
                "icon": SERVICE_ICONS[idx % len(SERVICE_ICONS)],
            }
        )
    return features


def build_meta(slug: str) -> PageMeta:
    title = slug_to_title(slug)
    desc = make_description(slug, title)
    template_key = choose_template(slug)
    breadcrumb_class = "bread_img_6" if template_key == "services" else ""
    return PageMeta(
        slug=slug,
        title=title,
        description=desc,
        breadcrumb=title,
        tagline=title.upper(),
        highlight_intro=f"Hoja de ruta para {title}",
        highlight_span="con Kiki Latam",
        stats=default_stats(),
        skills=default_skills(),
        stories=default_stories(title),
        features=default_features(title),
        breadcrumb_class=breadcrumb_class,
    )


def choose_template(slug: str) -> str:
    if slug in EXPLICIT_TEMPLATE:
        return EXPLICIT_TEMPLATE[slug]
    for prefix in TEAM_LIKE_PREFIXES:
        if slug.startswith(prefix):
            return "team"
    for prefix in SERVICE_LIKE_PREFIXES:
        if slug.startswith(prefix):
            return "services"
    for prefix in INFO_LIKE_PREFIXES:
        if slug.startswith(prefix):
            return "who"
    if slug.startswith("services-"):
        return "team"
    if slug.startswith("soluciones"):
        return "services"
    return "who"


def render_stats(meta: PageMeta) -> str:
    blocks = []
    for idx, stat in enumerate(meta.stats):
        icon = STAT_ICONS[idx % len(STAT_ICONS)]
        blocks.append(
            dedent(
                f"""
                <div class=\"col-xl-3 col-lg-3 col-md-6 col-sm-6\">
                    <div class=\"count_style d-flex align-items-center justify-content-center flex-column\">
                        <div class=\"counter_img\"><img src=\"{icon}\" alt=\"\"></div>
                        <div class=\"d-flex align-items-center mt-4\">
                            <div class=\"counter\" data-count-start=\"{stat['start']}\" data-count-end=\"{stat['end']}\" data-speed=\"40\"></div>
                            <span>{stat['suffix']}</span>
                        </div>
                        <h5>{stat['label']}</h5>
                    </div>
                </div>
                """
            ).strip()
        )
    return "\n".join(blocks)


def render_skills(meta: PageMeta) -> str:
    bars = []
    for skill in meta.skills:
        bars.append(
            dedent(
                f"""
                <div class=\"bar\">
                    <div class=\"info\">
                        <span>{skill['label']}</span>
                    </div>
                    <div class=\"progress-line {skill['class']}\">
                        <span></span>
                    </div>
                </div>
                """
            ).strip()
        )
    return "\n".join(bars)


def render_who(meta: PageMeta) -> str:
    stats = render_stats(meta)
    skills = render_skills(meta)
    return dedent(
        f"""
        <!-- breadrumb section start -->
        <section class=\"breadcrumb_section {meta.breadcrumb_class}\">
            <div class=\"container\">
                <div class=\"row\">
                    <div class=\"breadcrumb_content\">
                        <div class=\"row\">
                            <div class=\"col-xl-3 col-lg-3\"></div>
                            <div class=\"col-xl-6 col-lg-6\">
                                <div class=\"breadcrumb_heading text-center\">
                                    <h2>{meta.title}</h2>
                                    <p class=\"pairagraph mt-3\">{meta.description}</p>
                                </div>
                            </div>

                            <div class=\"breadcrumb_list\">
                                <ul class=\"d-flex list-unstyled p-0 m-0\">
                                    <li><a href=\"index.html\">Home</a></li>
                                    <li><i class=\"fa-solid fa-angles-right\"></i></li>
                                    <li>{meta.breadcrumb}</li>
                                </ul>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- breadrumb section end -->


        <!-- about section start -->

        <section class=\"about_section pt-100 \" data-aos=\"fade-up\" data-aos-duration=\"3000\">
            <div class=\"container\">
                <div class=\"row align-items-center\">
                    <div class=\"col-xl-5 col-lg-5 col-md-12\">
                        <div class=\"about_img_2\">
                            <img src=\"assets/images/about-2.png\" alt=\"\">
                        </div>
                    </div>
                    <div class=\"col-xl-7 col-lg-7 col-md-12 mt-md-0 mt-5\">
                        <div class=\"about_content padding_left\">
                            <h3 class=\"child_heading\">{meta.tagline}</h3>
                            <img src=\"assets/images/heading.png\" alt=\"\">
                            <h1 class=\"main_heading\">{meta.highlight_intro} <span style=\"color:#4b67c6;\">{meta.highlight_span}</span></h1>
                            <p class=\"pairagraph mt-3 text_justify\">Este es un módulo de contenido editable para introducir contexto, diferenciales y métricas clave.</p>
                            <div class=\"d-flex mt-4 gap-4\">
                                <div class=\"about_elements\">
                                    <img src=\"assets/images/icon/verified.gif\" alt=\"\">
                                </div>
                                <div class=\"content_box\">
                                    <h3 class=\"text-dark\">Promesa de valor</h3>
                                    <p class=\"pairagraph\">Resume el beneficio central y la propuesta específica de esta página.</p>
                                </div>
                            </div>
                            <div class=\"d-flex mt-2 gap-4\">
                                <div class=\"about_elements\">
                                    <img src=\"assets/images/icon/verified.gif\" alt=\"\">
                                </div>
                                <div class=\"content_box mb-4\">
                                    <h3 class=\"text-dark\">Próximos pasos</h3>
                                    <p class=\"pairagraph\">Detalla cómo activar el servicio, solución o recurso correspondiente.</p>
                                </div>
                            </div>
                            <a class=\"main_btn\" href=\"contact-us.html\">Hablar con un asesor <i class=\"fa-solid fa-angles-right\"></i></a>
                        </div>
                    </div>

                </div>
            </div>
        </section>

        <!-- about section end -->


        <!-- counter section start -->

        <div class=\"counter_section pt-100\">
            <div class=\"container\">
                <div class=\"top_content_heading text-center\">
                    <h3 class=\"child_heading text-white\">INDICADORES CLAVE</h3>
                    <img src=\"assets/images/white_heading.png\" alt=\"\">
                    <h2 class=\"main_heading text-white\">Contexto cuantitativo para {meta.title}</h2>
                </div>
                <div class=\"row mt-5\" data-aos=\"fade-up\" data-aos-duration=\"3000\">
{stats}
                </div>
            </div>
        </div>

        <!-- counter section end -->


        <!-- skill bar section start -->

        <section class=\"Skills_section pt-100\">
            <div class=\"container\">
                <div class=\"row\">
                    <div class=\"col-xl-6 col-lg-6 col-md-12\" data-aos=\"fade-right\" data-aos-offset=\"300\"
                        data-aos-easing=\"ease-in-sine\">
                        <div class=\"skill_content mt-5\">
                            <h3 class=\"child_heading \">MARCOS OPERATIVOS</h3>
                            <img src=\"assets/images/heading.png\" alt=\"\">
                            <h2 class=\"main_heading\">Capacidades que soportan {meta.title}</h2>
                            <p class=\"pairagraph mt-3 text_justify\">Describe la madurez operativa, pods y herramientas que habilitan esta iniciativa.</p>
                            <div class=\"skill-bars\">
{skills}
                            </div>

                        </div>
                    </div>
                    <div class=\"col-xl-6 col-lg-6 col-md-12 mt-lg-0 mt-5\">
                        <div class=\"skill_img\">
                            <img src=\"assets/images/skill-image.png\" alt=\"\">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- skill bar section end -->
        """
    ).strip()


def render_team(meta: PageMeta) -> str:
    story_blocks = []
    for idx, story in enumerate(meta.stories):
        reverse = idx % 2 == 1
        left_image = reverse
        image_col = (
            dedent(
                f"""
                <div class=\"col-md-4 mb-4{' mb-lg-0' if reverse else ''}\">
                    <img src=\"{story['image']}\" class=\"img-fluid\" alt=\"\">
                </div>
                """
            ).strip()
        )
        text_col = dedent(
            f"""
            <div class=\"col-md-7\">
                <div class=\"overflow-hidden\">
                    <h2 class=\"main_heading\">{story['heading']}</h2>
                    <h6>{story['role']}</h6>
                </div>
                <p class=\"pairagraph\">{story['description']}</p>
                <p class=\"pairagraph\">{story['secondary']}</p>
                <hr class=\"solid my-4\">
                <div class=\"row align-items-center mt-5\">
                    <div class=\"col-xl-6 col-lg-6 col-md-5 col-5\">
                        <a href=\"{story['cta_link']}\" class=\"btn-dark mt-3\">{story['cta']}</a>
                    </div>
                    <div class=\"col-xl-6 col-lg-6 col-md-7 col-7\">
                        <div class=\"d-flex align-items-center justify-content-end\">
                            <strong class=\"text-uppercase\">Compartir</strong>
                            <ul class=\"social_icons\">
                                <li class=\"social-icons-facebook\"><a href=\"javascript:void(0)\" title=\"Facebook\"><i class=\"fab fa-facebook-f\"></i></a></li>
                                <li class=\"social-icons-x\"><a href=\"javascript:void(0)\" title=\"X\"><i class=\"fab fa-x-twitter\"></i></a></li>
                                <li class=\"social-icons-linkedin\"><a href=\"javascript:void(0)\" title=\"Linkedin\"><i class=\"fab fa-linkedin-in\"></i></a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            """
        ).strip()
        row = (
            dedent(
                f"""
                <div class=\"row\" data-aos=\"fade-up\" data-aos-duration=\"3000\">
                    {'<div class="col-md-1"></div>'.join([''] * 0)}
                </div>
                """
            ).strip()
        )
        content_cols = (
            f"<div class=\"col-md-1\"></div>" if reverse else f"<div class=\"col-md-1\"></div>"
        )
        # Build row manually to retain spacing
        if reverse:
            block = (
                "<div class=\"row\" data-aos=\"fade-up\" data-aos-duration=\"3000\">\n"
                f"    {image_col}\n"
                "    <div class=\"col-md-1\"></div>\n"
                f"    {text_col}\n"
                "</div>"
            )
        else:
            block = (
                "<div class=\"row\" data-aos=\"fade-up\" data-aos-duration=\"3000\">\n"
                f"    {text_col}\n"
                "    <div class=\"col-md-1\"></div>\n"
                f"    {image_col}\n"
                "</div>"
            )
        story_blocks.append(block)
        if idx != len(meta.stories) - 1:
            story_blocks.append("<hr class=\"solid my-5\">")
    stories_html = "\n".join(story_blocks)
    return dedent(
        f"""
        <!-- breadrumb section start -->
        <section class=\"breadcrumb_section {meta.breadcrumb_class}\">
            <div class=\"container\">
                <div class=\"row\">
                    <div class=\"breadcrumb_content\">
                        <div class=\"row\">
                            <div class=\"col-xl-3 col-lg-3\"></div>
                            <div class=\"col-xl-6 col-lg-6\">
                                <div class=\"breadcrumb_heading text-center\">
                                    <h2>{meta.title}</h2>
                                    <p class=\"pairagraph mt-3\">{meta.description}</p>
                                </div>
                            </div>

                            <div class=\"breadcrumb_list\">
                                <ul class=\"d-flex list-unstyled p-0 m-0\">
                                    <li><a href=\"index.html\">Home</a></li>
                                    <li><i class=\"fa-solid fa-angles-right\"></i></li>
                                    <li>{meta.breadcrumb}</li>
                                </ul>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- breadrumb section end -->


        <!--our_team_section start  -->

        <section class=\"our_team_section pt-100\">
            <div class=\"container\">
{stories_html}
            </div>
        </section>

        <!--our_team_section end  -->
        """
    ).strip()


def render_services(meta: PageMeta) -> str:
    card_blocks = []
    for feature in meta.features:
        card_blocks.append(
            dedent(
                f"""
                <div class=\"col-xl-4 col-lg-4 col-md-4 mt-3\">
                    <div class=\"services_box_3\">
                        <div class=\"services_icon\">
                            <img src=\"{feature['icon']}\" alt=\"\">
                        </div>
                        <h4 class=\"mt-3\">{feature['title']}</h4>
                        <p class=\"pairagraph mt-2 mb-0\">{feature['copy']}</p>
                        <div class=\"read_more mt-2\">
                            <a href=\"contact-us.html\">Hablar con ventas<i class=\"fa-solid fa-angles-right\"></i></a>
                        </div>
                    </div>
                </div>
                """
            ).strip()
        )
    cards_html = "\n".join(card_blocks)
    return dedent(
        f"""
        <!-- breadrumb section start -->

        <section class=\"breadcrumb_section {meta.breadcrumb_class}\">
            <div class=\"container\">
                <div class=\"row\">
                    <div class=\"breadcrumb_content\">
                        <div class=\"row\">
                            <div class=\"col-xl-3 col-lg-3\"></div>
                            <div class=\"col-xl-6 col-lg-6\">
                                <div class=\"breadcrumb_heading text-center\">
                                    <h2>{meta.title}</h2>
                                    <p class=\"pairagraph mt-3\">{meta.description}</p>
                                </div>
                            </div>

                            <div class=\"breadcrumb_list\">
                                <ul class=\"d-flex list-unstyled p-0 m-0\">
                                    <li><a href=\"index.html\">Home</a></li>
                                    <li><i class=\"fa-solid fa-angles-right\"></i></li>
                                    <li>{meta.breadcrumb}</li>
                                </ul>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- breadrumb section end -->


        <!-- our services section start -->

        <section class=\"our_services_3 pt-100\">
            <div class=\"container\">
                <div class=\"top_content_heading \">
                    <h3 class=\"child_heading \">Componentes clave</h3>
                    <img src=\"assets/images/heading.png\" alt=\"\">
                    <h2 class=\"main_heading\">Roadmap para {meta.title}</h2>
                    <p class=\"pairagraph mt-2\">Utiliza estas tarjetas como guía para documentar beneficios, entregables y responsables.</p>
                </div>

                <div class=\"row\" data-aos=\"fade-up\" data-aos-duration=\"3000\">
{cards_html}
                </div>
            </div>

        </section>

        <!-- our services section end -->


        <!-- get in touch section start -->

        <section class=\"Get_in_touch pt-100\">
            <div class=\"container\">
                <div class=\"text-center\">
                    <h3 class=\"child_heading\">Siguiente paso</h3>
                    <img src=\"assets/images/heading.png\" alt=\"\">
                    <h2 class=\"main_heading\">Agenda una sesión para profundizar en {meta.title}</h2>
                    <p class=\"pairagraph\">Usa este formulario como punto de partida para captar leads o solicitudes internas.</p>
                </div>

                <div class=\"row align-items-center mt-5\">
                    <div class=\"shepe_round\">
                        <div class=\"element-1\">
                            <img src=\"assets/images/shape/shap-1.png\" alt=\"\">
                        </div>
                        <div class=\"element-2\">
                            <img src=\"assets/images/shape/shape2.png\" alt=\"\">
                        </div>
                    </div>

                    <div class=\"col-xl-7 col-lg-7 col-md-12\" data-aos=\"fade-right\" data-aos-offset=\"300\"
                        data-aos-easing=\"ease-in-sine\">
                        <div class=\"talk_form_box\">
                            <form id=\"contactForm\">
                                <div class=\"row mt-3\">
                                    <div class=\"col-md-6 col-sm-6\">
                                        <div class=\"mb-3\">
                                            <label class=\"form-label\">Nombre</label>
                                            <input type=\"text\" id=\"name\" name=\"user-name\" placeholder=\"Escribe tu nombre\">
                                        </div>
                                    </div>
                                    <div class=\"col-md-6 col-sm-6\">
                                        <div class=\"mb-3\">
                                            <label class=\"form-label\">Email*</label>
                                            <input type=\"email\" id=\"email\" name=\"email\"
                                                placeholder=\"Ingresa tu correo\">
                                        </div>
                                    </div>
                                </div>
                                <div class=\"row mt-3\">
                                    <div class=\"col-md-6 col-sm-6\">
                                        <div class=\"mb-3\">
                                            <label class=\"form-label\">Teléfono*</label>
                                            <input type=\"number\" id=\"contactNumber\" name=\"phone-no\"
                                                placeholder=\"+57 000 0000\">
                                        </div>
                                    </div>
                                    <div class=\"col-md-6 col-sm-6\">
                                        <div class=\"mb-3\">
                                            <label class=\"form-label\">Requerimiento*</label>
                                            <input type=\"text\" id=\"requirement\" name=\"requirement\"
                                                placeholder=\"Cuéntanos qué necesitas\">
                                        </div>
                                    </div>
                                    <div class=\"col-xl-12 col-lg-12\">
                                        <div class=\"mb-3\">
                                            <label class=\"form-label\" for=\"message\">Mensaje</label>
                                            <textarea id=\"message\" name=\"message\" rows=\"5\" cols=\"5\"
                                                placeholder=\"Comparte más contexto\"></textarea>
                                        </div>
                                    </div>
                                </div>
                                <div class=\"d-flex justify-content-center mt-3\">
                                    <button type=\"submit\" name=\"submit\" class=\"main_btn text-white\">Enviar mensaje
                                        &nbsp;&nbsp;<i class=\"fa fa-spinner fa-spin\"
                                            style=\"font-size:20px; display: none; float: right;\"></i></button>
                                </div>
                            </form>

                        </div>

                    </div>

                    <div class=\"col-xl-5 col-lg-5 col-md-12 mt-lg-0 mt-5\" data-aos=\"fade-left\"
                        data-aos-anchor=\"#example-anchor\" data-aos-offset=\"500\" data-aos-duration=\"500\">
                        <div class=\"get_img p-2 \">
                            <img src=\"assets/images/get_img.jpeg\" alt=\"\">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- get in touch section end -->
        """
    ).strip()


def render_template(template_name: str, meta: PageMeta) -> str:
    if template_name == "who":
        return render_who(meta)
    if template_name == "team":
        return render_team(meta)
    if template_name == "services":
        return render_services(meta)
    raise ValueError(f"Unknown template '{template_name}'")


def replace_center_block(file_path: Path, new_block: str) -> bool:
    content = file_path.read_text(encoding="utf-8")
    favicon_updated = False
    if FAVICON_OLD in content:
        content = content.replace(FAVICON_OLD, FAVICON_NEW)
        favicon_updated = True

    updated = False
    start = content.find("<!-- breadrumb section start -->")
    end = content.find("<!-- footer section start -->")
    if start != -1 and end != -1 and start < end:
        content = content[:start] + new_block + "\n\n" + content[end:]
        updated = True
    else:
        alt_start = content.find("<main class=\"internal-page\"")
        if alt_start != -1:
            alt_end = content.find("</main>", alt_start)
            if alt_end != -1:
                block_end = alt_end + len("</main>")
                content = content[:alt_start] + new_block + "\n\n" + content[block_end:]
                updated = True

    if updated or favicon_updated:
        file_path.write_text(content, encoding="utf-8")
    return updated or favicon_updated


def ensure_favicon(file_path: Path) -> bool:
    content = file_path.read_text(encoding="utf-8")
    if FAVICON_OLD not in content:
        return False
    content = content.replace(FAVICON_OLD, FAVICON_NEW)
    file_path.write_text(content, encoding="utf-8")
    return True


def process_file(file_path: Path) -> None:
    slug = file_path.stem
    if file_path.name in PRESERVE_LAYOUT:
        if ensure_favicon(file_path):
            print(f"✔ Updated favicon in {file_path.name}")
        else:
            print(f"• Skipped {file_path.name}")
        return
    template_name = choose_template(slug)
    meta = build_meta(slug)
    block = render_template(template_name, meta)
    changed = replace_center_block(file_path, block)
    status = "✔" if changed else "•"
    print(f"{status} Applied '{template_name}' template to {file_path.name}")


def main() -> None:
    html_files = sorted(ROOT.glob(HTML_GLOB))
    for html_file in html_files:
        process_file(html_file)


if __name__ == "__main__":  # pragma: no cover
    main()

from __future__ import annotations

import html
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "index.html"
OUTPUT_DIR = ROOT

index_text = INDEX_PATH.read_text(encoding="utf-8")

HEADER_START = "    <!-- loader start -->"
HEADER_END = "    <!-- hero_section start -->"
FOOTER_START = "    <!-- footer section start -->"
JS_START = "    <!-- js link start -->"

if HEADER_START not in index_text or HEADER_END not in index_text:
    raise RuntimeError("No se encontraron los marcadores de cabecera en index.html")

if FOOTER_START not in index_text or JS_START not in index_text:
    raise RuntimeError("No se encontró el bloque de pie de página o scripts en index.html")

header_block = index_text[index_text.index(HEADER_START): index_text.index(HEADER_END)]
footer_block = index_text[index_text.index(FOOTER_START): index_text.index(JS_START)]

DEFAULT_METRICS = (
    ("Estado", "Listo", "Estructura y estilos cargados"),
    ("Tiempo", "< 1 semana", "Solo falta contenido"),
    ("Equipo", "Pods Kiki", "Diseño + contenido a la espera"),
)

DEFAULT_CARDS = (
    "Brief táctico para el foco indicado",
    "Stack recomendado y dependencias críticas",
    "Checklist de assets y métricas para cargar"
)

DEFAULT_MODULES = (
    ("Diagnóstico", "Mapa de retos y KPIs base"),
    ("Pods y herramientas", "Integraciones y equipos que intervienen"),
    ("Roadmap 30-60-90", "Entregables y próximas decisiones")
)


def make_page(filename: str, title: str, summary: str, focus: str, category: str,
              primary_cta: str = "Solicitar propuesta",
              primary_href: str = "contact-us.html",
              secondary_cta: str = "Ver capabilities",
              secondary_href: str = "services.html") -> dict:
    return {
        "filename": filename,
        "title": title,
        "summary": summary,
        "focus": focus,
        "category": category,
        "primary_cta": primary_cta,
        "primary_href": primary_href,
        "secondary_cta": secondary_cta,
        "secondary_href": secondary_href,
    }


PAGES = [
    make_page("about.html", "Conoce a Kiki", "Historia, equipo y cultura que impulsan nuestras operaciones.", "historia y cultura", "Acerca de"),
    make_page("capacidad-crossborder.html", "Capacidad: Cross-border", "Gestión aduanal y MoR para vender como local.", "operaciones cross-border", "Cobertura"),
    make_page("capacidad-devoluciones.html", "Capacidad: Reverse & QA", "Devoluciones y refurb centralizados.", "reverse logistics", "Cobertura"),
    make_page("capacidad-fulfillment-latam.html", "Capacidad: Fulfillment regional", "Bodegas con WMS unificado y prep center.", "fulfillment regional", "Cobertura"),
    make_page("capacidad-ultima-milla.html", "Capacidad: Última milla", "Promesa 24-72h con control de carriers.", "última milla", "Cobertura"),
    make_page("caso-cash-flow.html", "Caso: Optimizar cash flow", "Adelantos y control de ciclos financieros.", "cash flow", "Casos típicos"),
    make_page("caso-cod-latam.html", "Caso: Vender en LATAM con COD", "Cash on Delivery seguro y conciliado.", "cash on delivery", "Casos típicos"),
    make_page("caso-escalar-operaciones.html", "Caso: Escalar operaciones", "Playbooks de fulfillment + pagos integrados.", "escalar operaciones", "Casos típicos"),
    make_page("caso-us-sin-empresa.html", "Caso: Vender en US sin empresa", "Entrada express con cumplimiento fiscal.", "entrada a US", "Casos típicos"),
    make_page("casos-benchmarks.html", "Casos: Benchmarks por industria", "Niveles de NPS, conversión y SLA.", "benchmarks", "Casos"),
    make_page("casos-checkout.html", "Casos: Checkout & BNPL", "Conversión +18% con métodos locales.", "checkout y BNPL", "Casos"),
    make_page("casos-ecommerce.html", "Casos: E-commerce & D2C", "Escala de 500 a 5.000 órdenes al día.", "e-commerce", "Casos"),
    make_page("casos-fulfillment.html", "Casos: Fulfillment regional", "Pick & pack con SLA 99%.", "fulfillment", "Casos"),
    make_page("casos-marketplace.html", "Casos: Marketplaces & sellers PRO", "Inventario sincronizado y cashflow controlado.", "marketplaces", "Casos"),
    make_page("casos-mor.html", "Casos: Merchant of Record", "Operaciones cross-border sin entidad.", "merchant of record", "Casos"),
    make_page("casos-retail-omnicanal.html", "Casos: Retail omnicanal", "Click & collect, dark stores y devoluciones ágiles.", "retail omnicanal", "Casos"),
    make_page("casos-subscriptions.html", "Casos: Suscripciones & clubes", "LTV alto con fulfillment predictivo.", "suscripciones", "Casos"),
    make_page("casos-testimonios.html", "Casos: Testimonios ejecutivos", "CMOs y COOs cuentan su playbook.", "testimonios", "Casos"),
    make_page("casos-ultima-milla.html", "Casos: Última milla", "Cobertura LATAM con promesa 24-72h.", "última milla", "Casos"),
    make_page("cobertura-colombia.html", "Cobertura: Colombia", "Bogotá, Medellín y red de última milla.", "cobertura Colombia", "Cobertura"),
    make_page("cobertura-mexico.html", "Cobertura: México", "CDMX, Monterrey y hubs fronterizos.", "cobertura México", "Cobertura"),
    make_page("cobertura-peru.html", "Cobertura: Perú", "Callao fulfillment + Lima same day.", "cobertura Perú", "Cobertura"),
    make_page("cobertura-usa.html", "Cobertura: Estados Unidos", "Miami fulfillment como gateway cross-border.", "cobertura USA", "Cobertura"),
    make_page("index-2.html", "Landing alternativa", "Versión experimental del home y hero principal.", "landing experimental", "Prototipos", secondary_href="index.html"),
    make_page("perfil-cpa.html", "Perfil: Afiliados / CPA", "COD, BNPL y cashflow para media buyers.", "afiliados y CPA", "Para quién es"),
    make_page("perfil-crossborder.html", "Perfil: Cross-border & Enterprise", "Expansión con MoR, reporting y compliance.", "cross-border enterprise", "Para quién es"),
    make_page("perfil-ecommerce.html", "Perfil: E-commerce / D2C", "Conversión y promesas de entrega consistentes.", "e-commerce D2C", "Para quién es"),
    make_page("perfil-marketplace.html", "Perfil: Marketplaces", "Operación multi-país con pagos locales.", "marketplaces", "Para quién es"),
    make_page("recurso-api-integraciones.html", "Recurso: Centro de integraciones", "Documentación API y SDKs.", "integraciones", "Recursos", secondary_href="blog.html", secondary_cta="Ver hub"),
    make_page("recurso-benchmark-checkout.html", "Recurso: Benchmarks de checkout", "Conversión por país y método de pago.", "benchmarks de checkout", "Recursos", secondary_href="blog.html", secondary_cta="Ir a recursos"),
    make_page("recurso-calculadora-fulfillment.html", "Recurso: Calculadora de fulfillment", "Simula costos por país y SKU.", "calculadora de fulfillment", "Recursos", secondary_href="blog.html", secondary_cta="Ir a recursos"),
    make_page("recurso-guia-cod.html", "Recurso: Guía COD LATAM", "Estructura, contracargos y cashflow.", "guía COD", "Recursos", secondary_href="blog.html", secondary_cta="Ir a recursos"),
    make_page("recurso-playbook-expansion.html", "Recurso: Playbook de expansión", "Checklist legal, fiscal y operativo.", "playbook de expansión", "Recursos", secondary_href="blog.html", secondary_cta="Ver recursos"),
    make_page("recurso-webinars.html", "Recurso: Webinars & workshops", "Sesiones con marcas que ya escalaron.", "webinars", "Recursos", secondary_href="blog.html", secondary_cta="Ir a recursos"),
    make_page("services-2.html", "Servicios complementarios", "Catálogo de casos por servicio y variantes.", "servicios complementarios", "Servicios"),
    make_page("services-3.html", "Servicios: Testimonios ejecutivos", "Historias que conectan operaciones y negocio.", "testimonios", "Servicios"),
    make_page("servicio-almacenamiento.html", "Servicio: Almacenamiento", "Inventario smart y balance regional.", "almacenamiento", "Servicios"),
    make_page("servicio-bnpl.html", "Servicio: BNPL", "Cuotas y financiamiento instantáneo.", "BNPL", "Servicios"),
    make_page("servicio-checkout-point.html", "Servicio: Checkout Point", "Checkout omnicanal con códigos locales.", "checkout point", "Servicios"),
    make_page("servicio-cod.html", "Servicio: Cash on Delivery", "Gestión y conciliación de cobranza COD.", "cash on delivery", "Servicios"),
    make_page("servicio-cross-border.html", "Servicio: Cross-border LATAM & US", "Envía y cobra en dos continentes.", "cross-border LATAM & US", "Servicios"),
    make_page("servicio-fulfillment.html", "Servicio: Fulfillment", "Centros certificados en LATAM y US.", "fulfillment", "Servicios"),
    make_page("servicio-merchant-of-record.html", "Servicio: Merchant of Record", "Facturación y cumplimiento tributario.", "merchant of record", "Servicios"),
    make_page("servicio-prepaid.html", "Servicio: Prepaid", "Cobros anticipados y antifraude.", "prepaid", "Servicios"),
    make_page("servicio-ultima-milla.html", "Servicio: Última milla", "Red propia y partners certificados.", "última milla", "Servicios"),
    make_page("solucion-cobrar-local.html", "Solución: Cobrar localmente", "Pagos locales, BNPL y MoR regulado.", "cobrar local", "Soluciones", secondary_href="solutions.html"),
    make_page("solucion-entregar-mejor.html", "Solución: Entregar mejor", "SLA de última milla y control de promise date.", "entregar mejor", "Soluciones", secondary_href="solutions.html"),
    make_page("solucion-expandirse.html", "Solución: Expandirse sin entidad", "Operamos como Merchant of Record multi-país.", "expandirse sin entidad", "Soluciones", secondary_href="solutions.html"),
    make_page("solucion-vender-mas.html", "Solución: Vender más", "Optimiza funnels, checkout y remarketing local.", "vender más", "Soluciones", secondary_href="solutions.html"),
]

HEAD_TEMPLATE = dedent(
    """
    <!DOCTYPE html>
    <html lang=\"es\">
    <head>
        <meta charset=\"UTF-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
        <title>{title} | Kiki Latam</title>
        <meta name=\"description\" content=\"{description}\">
        <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css\" />
        <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>
        <link href=\"https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300..900;1,300..900&display=swap\" rel=\"stylesheet\">
        <link rel=\"icon\" href=\"assets/images/favicon.png\" sizes=\"32x32\" />
        <link rel=\"stylesheet\" href=\"assets/css/style.css\" />
        <link rel=\"stylesheet\" href=\"assets/css/responsive.css\" />
        <link rel=\"stylesheet\" href=\"assets/css/aos.css\" />
        <link rel=\"stylesheet\" href=\"assets/css/bootstrap-grid.css\" />
        <link rel=\"stylesheet\" href=\"assets/css/bootstrap-reboot.css\" />
        <link rel=\"stylesheet\" href=\"assets/css/bootstrap-utilities.css\" />
        <link rel=\"stylesheet\" href=\"assets/css/bootstrap.css\" />
        <link rel=\"stylesheet\" href=\"assets/css/bootstrap.min.css\" />
        <link rel=\"stylesheet\" href=\"assets/css/bootstrap.rtl.css\" />
        <link rel=\"stylesheet\" href=\"assets/css/swiper-bundle.min.css\" />
    </head>
    <body>
    """
)

CONTENT_TEMPLATE = dedent(
    """
        <main class=\"internal-page\" data-focus=\"{focus}\">
            <section class=\"internal-hero\">
                <div class=\"internal-badge\">{category}</div>
                <h1>{title}</h1>
                <p class=\"lead\">{summary}</p>
                <ul class=\"hero-metrics\">
                    {metrics}
                </ul>
                <div class=\"hero-ctas\">
                    <a class=\"main_btn\" href=\"{primary_href}\">{primary_cta}</a>
                    <a class=\"btn-link\" href=\"{secondary_href}\">{secondary_cta} →</a>
                </div>
            </section>

            <section class=\"internal-grid\">
                <div class=\"grid-heading\">
                    <h3>Qué preparamos para {focus}</h3>
                    <p>Esta landing está lista para recibir textos, módulos visuales y casos que detallen el foco descrito.</p>
                </div>
                <div class=\"internal-cards\">
                    {cards}
                </div>
            </section>

            <section class=\"internal-modules\">
                <div class=\"grid-heading\">
                    <h3>Módulos listos</h3>
                    <p>Solo falta reemplazar el copy y las imágenes según los insumos finales.</p>
                </div>
                <div class=\"module-list\">
                    {modules}
                </div>
            </section>

            <section class=\"internal-cta\">
                <div>
                    <h3>Siguiente paso</h3>
                    <p>Cargaremos los assets y validaremos con el equipo de contenido en cuanto estén listos.</p>
                </div>
                <a class=\"main_btn\" href=\"contact-us.html\">Coordinar entrega</a>
            </section>
        </main>
    """
)

SCRIPTS_BLOCK = dedent(
    """
        <script src=\"https://code.jquery.com/jquery-3.7.1.min.js\" integrity=\"sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=\" crossorigin=\"anonymous\"></script>
        <script src=\"https://cdn.jsdelivr.net/npm/sweetalert2@11\"></script>
        <script src=\"https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js\"></script>
        <script src=\"assets/js/aos.js\"></script>
        <script src=\"assets/js/function.js\"></script>
        <script src=\"assets/js/script.js\"></script>
        <script src=\"assets/js/code.js\"></script>
        <script src=\"assets/js/popup.js\"></script>
        <script src=\"assets/js/bootstrap.bundle.js\"></script>
        <script src=\"assets/js/bootstrap.bundle.min.js\"></script>
        <script src=\"assets/js/bootstrap.js\"></script>
        <script src=\"assets/js/bootstrap.min.js\"></script>
    </body>
    </html>
    """
)


def render_metrics(focus: str) -> str:
    parts = []
    for label, value, desc in DEFAULT_METRICS:
        parts.append(
            f"<li><span>{html.escape(value)}</span><small>{html.escape(label)}</small><p>{html.escape(desc)}</p></li>"
        )
    return "".join(parts)


def render_cards(focus: str) -> str:
    items = []
    for text in DEFAULT_CARDS:
        items.append(f"<article class=\"internal-card\"><p>{html.escape(text.replace('el foco indicado', focus))}</p></article>")
    return "".join(items)


def render_modules() -> str:
    blocks = []
    for title, desc in DEFAULT_MODULES:
        blocks.append(
            f"<article><h4>{html.escape(title)}</h4><p>{html.escape(desc)}</p><span class=\"tag\">Pendiente de assets</span></article>"
        )
    return "".join(blocks)


def build_page(page: dict) -> str:
    description = html.escape(page["summary"])
    head = HEAD_TEMPLATE.format(title=html.escape(page["title"]), description=description)
    metrics_html = render_metrics(page["focus"])
    cards_html = render_cards(page["focus"])
    modules_html = render_modules()
    content = CONTENT_TEMPLATE.format(
        focus=html.escape(page["focus"]),
        category=html.escape(page["category"]),
        title=html.escape(page["title"]),
        summary=description,
        metrics=metrics_html,
        primary_cta=html.escape(page["primary_cta"]),
        primary_href=html.escape(page["primary_href"]),
        secondary_cta=html.escape(page["secondary_cta"]),
        secondary_href=html.escape(page["secondary_href"]),
        cards=cards_html,
        modules=modules_html,
    )
    return head + header_block + content + footer_block + SCRIPTS_BLOCK


def main() -> None:
    created = []
    skipped = []
    for page in PAGES:
        target = OUTPUT_DIR / page["filename"]
        if target.exists():
            skipped.append(page["filename"])
            continue
        target.write_text(build_page(page), encoding="utf-8")
        created.append(page["filename"])
    print(f"Created {len(created)} pages")
    if skipped:
        print(f"Skipped {len(skipped)} existing pages")


if __name__ == "__main__":
    main()

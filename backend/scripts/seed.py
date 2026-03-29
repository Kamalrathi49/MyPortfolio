import uuid

from sqlalchemy import delete

from app.db.session import SessionLocal, get_engine
from app.models.project import Project
from app.models.skill import Skill, SkillCategory
from app.models.work_experience import WorkExperience


def run() -> None:
    db = SessionLocal(bind=get_engine())
    try:
        db.execute(delete(Skill))
        db.execute(delete(SkillCategory))
        db.execute(delete(Project))
        db.execute(delete(WorkExperience))
        db.commit()

        cat_backend = SkillCategory(
            id=uuid.uuid4(),
            name="Backend",
            sort_order=0,
        )
        cat_db = SkillCategory(
            id=uuid.uuid4(),
            name="Databases",
            sort_order=1,
        )
        cat_async = SkillCategory(
            id=uuid.uuid4(),
            name="Async & distributed systems",
            sort_order=2,
        )
        cat_int = SkillCategory(
            id=uuid.uuid4(),
            name="Integrations",
            sort_order=3,
        )
        cat_devops = SkillCategory(
            id=uuid.uuid4(),
            name="DevOps & infrastructure",
            sort_order=4,
        )
        cat_fe = SkillCategory(
            id=uuid.uuid4(),
            name="Frontend (working knowledge)",
            sort_order=5,
        )
        db.add_all(
            [
                cat_backend,
                cat_db,
                cat_async,
                cat_int,
                cat_devops,
                cat_fe,
            ]
        )
        db.flush()

        def sk(
            cid,
            name,
            prof,
            years,
            highlights,
            order,
        ):
            return Skill(
                id=uuid.uuid4(),
                category_id=cid,
                name=name,
                proficiency=prof,
                years=years,
                highlights=highlights,
                sort_order=order,
            )

        db.add_all(
            [
                sk(cat_backend.id, "Python", 5, 3, ["APIs", "services", "tooling"], 0),
                sk(cat_backend.id, "Django", 5, 3, ["ORM", "admin", "auth"], 1),
                sk(
                    cat_backend.id,
                    "Django REST Framework",
                    5,
                    3,
                    ["serializers", "viewsets", "permissions"],
                    2,
                ),
                sk(cat_backend.id, "FastAPI", 4, 2, ["OpenAPI", "deps", "async-ready"], 3),
                sk(cat_backend.id, "REST API design", 5, 3, ["versioning", "errors", "contracts"], 4),
                sk(cat_backend.id, "JWT authentication", 4, 3, ["tokens", "refresh flows"], 5),
                sk(cat_db.id, "PostgreSQL", 5, 3, ["indexing", "query tuning", "migrations"], 0),
                sk(cat_db.id, "MySQL", 4, 2, ["schemas", "replication-aware design"], 1),
                sk(cat_async.id, "Celery", 5, 3, ["queues", "retries", "schedules"], 0),
                sk(cat_async.id, "Redis", 5, 3, ["cache", "broker", "rate limits"], 1),
                sk(cat_async.id, "RabbitMQ", 4, 2, ["routing", "reliability"], 2),
                sk(cat_async.id, "Azure Queue", 4, 2, ["cloud jobs", "backpressure"], 3),
                sk(cat_int.id, "Razorpay", 4, 2, ["subscriptions", "webhooks"], 0),
                sk(cat_int.id, "Stripe", 4, 2, ["billing events", "idempotency"], 1),
                sk(cat_int.id, "Amazon SP-API", 4, 2, ["reports", "orders"], 2),
                sk(cat_int.id, "Facebook Ads API", 4, 2, ["insights", "pipelines"], 3),
                sk(cat_int.id, "Amazon Ads API", 4, 2, ["campaign data", "ETL"], 4),
                sk(cat_devops.id, "Docker", 5, 3, ["images", "compose", "deploy artifacts"], 0),
                sk(cat_devops.id, "CI/CD pipelines", 4, 3, ["automated builds", "releases"], 1),
                sk(cat_devops.id, "Git", 5, 4, ["branching", "reviews"], 2),
                sk(cat_devops.id, "Linux", 4, 3, ["shell", "ops", "debugging"], 3),
                sk(cat_devops.id, "Azure", 4, 2, ["queues", "hosting", "managed services"], 4),
                sk(cat_fe.id, "JavaScript", 4, 3, ["ES modules", "API clients"], 0),
                sk(cat_fe.id, "React", 3, 2, ["integration", "component boundaries"], 1),
            ]
        )

        gh = "https://github.com/kamalrathi49"

        db.add_all(
            [
                Project(
                    title="Yugyog.ai — AI CCTV analytics",
                    slug="yugyog-ai",
                    summary="Real-time detection backend for 500+ camera streams: events, billing, and queue-driven processing.",
                    description=(
                        "Backend for an AI CCTV platform ingesting people-counting, object detection, "
                        "and line-crossing events at scale. Focused on reliable pipelines, subscription "
                        "lifecycle, and low-latency handoff between edge inference and core services."
                    ),
                    impact_highlights=[
                        "Subscription system covering full lifecycle with real-time triggers.",
                        "Raised throughput and cut tail latency on high-volume AI event ingestion.",
                        "Stabilized detection pipelines across 500+ concurrent camera feeds.",
                    ],
                    tech_stack=[
                        "Django",
                        "DRF",
                        "Celery",
                        "Redis",
                        "PostgreSQL",
                        "Azure Queue",
                        "Razorpay",
                    ],
                    repo_url=gh,
                    demo_url=None,
                    featured=True,
                    sort_order=0,
                ),
                Project(
                    title="Spolto — fitness platform",
                    slug="spolto",
                    summary="Production APIs for a fitness product serving roughly 10K–50K active users with emphasis on uptime and clarity.",
                    description=(
                        "Owned core backend features for a high-traffic consumer app: traffic-shaped "
                        "endpoints, integrations, and operational visibility so the client stays fast "
                        "under load."
                    ),
                    impact_highlights=[
                        "Scaled REST surfaces for sustained peak traffic without brittle shortcuts.",
                        "Structured logging and monitoring hooks for faster incident diagnosis.",
                        "Normalized API responses to speed frontend delivery and reduce regressions.",
                    ],
                    tech_stack=["Django", "DRF", "PostgreSQL", "Amazon SNS", "Docker"],
                    repo_url=gh,
                    demo_url=None,
                    featured=True,
                    sort_order=1,
                ),
                Project(
                    title="Portfolio — FastAPI & React",
                    slug="portfolio-fullstack",
                    summary="Full-stack portfolio with API-driven content, rate limits, SMTP contact flow, and layered FastAPI architecture.",
                    description=(
                        "End-to-end build showcasing how I structure services: routers, domain services, "
                        "strict validation, and operational middleware—paired with a React UI that consumes "
                        "the same contracts recruiters can read in OpenAPI."
                    ),
                    impact_highlights=[
                        "Layered FastAPI layout (routers, services, schemas, core, db).",
                        "Per-IP rate limits, structured errors, and request logging with timing.",
                        "Background SMTP for contact while returning fast 202 responses to users.",
                    ],
                    tech_stack=["FastAPI", "React", "PostgreSQL", "Tailwind CSS", "Docker"],
                    repo_url=gh,
                    demo_url="https://kamalrathi.dev",
                    featured=True,
                    sort_order=2,
                ),
                Project(
                    title="Scalable API demo",
                    slug="scalable-api-demo",
                    summary="Reference design for caching, query discipline, and API ergonomics beyond basic CRUD.",
                    description=(
                        "A compact service layout demonstrating cache-friendly reads, bounded queries, "
                        "and clear boundaries—useful as a template for greenfield APIs."
                    ),
                    impact_highlights=[
                        "Shows system-design thinking: caching layers and hot-path optimization.",
                        "Documents patterns for consistent errors and versioning.",
                    ],
                    tech_stack=["FastAPI", "Redis", "PostgreSQL"],
                    repo_url=gh,
                    demo_url=None,
                    featured=False,
                    sort_order=3,
                ),
            ]
        )

        db.add_all(
            [
                WorkExperience(
                    id=uuid.uuid4(),
                    role="Software Developer",
                    company="CreateBytes",
                    period="May 2023 – Present",
                    summary=(
                        "Shipping production backends where performance, scale, and maintainable design "
                        "matter—APIs, data access, and deployment paths that teams can run safely."
                    ),
                    key_points=[
                        "Cut median API latency ~30% on hot paths via profiling-driven DRF and Django changes.",
                        "Split monolith modules into services to reduce deploy blast radius and coupling.",
                        "Tuned PostgreSQL indexes and queries for heavy endpoints (~25% faster p95 page loads).",
                        "Dockerized workloads and tightened CI/CD so releases are repeatable.",
                        "Mentored juniors and raised bar via reviews, patterns, and shared checklists.",
                    ],
                    sort_order=0,
                ),
                WorkExperience(
                    id=uuid.uuid4(),
                    role="Software Developer Intern",
                    company="WeSolveForYou",
                    period="Feb 2022 – Feb 2023",
                    summary=(
                        "Built and hardened integrations and reporting pipelines across ads and "
                        "marketplace APIs—emphasis on accurate, reconciled data at the warehouse edge."
                    ),
                    key_points=[
                        "Wired Amazon SP-API, Facebook Ads API, and Amazon Ads API into unified reporting.",
                        "Reduced cross-source inconsistencies by tightening validation and sync windows.",
                        "Refactored legacy Django areas for speed and clearer ownership boundaries.",
                    ],
                    sort_order=1,
                ),
            ]
        )
        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    run()

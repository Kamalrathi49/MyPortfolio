import { motion, useReducedMotion } from 'framer-motion'
import type { ProjectsResponse } from '../../lib/api'
import { Section } from '../ui/Section'

type ProjectsProps = {
  data: ProjectsResponse | null
  loading: boolean
  error: string | null
}

export function Projects({ data, loading, error }: ProjectsProps) {
  const reduce = useReducedMotion()
  const items = data?.items ?? []

  return (
    <Section id="projects" eyebrow="Work" title="Projects">
      {loading ? (
        <p className="text-slate-500">Loading projects…</p>
      ) : error ? (
        <p className="text-amber-400/90">{error}</p>
      ) : items.length === 0 ? (
        <p className="text-slate-500">No projects yet.</p>
      ) : (
        <div className="grid gap-6 md:grid-cols-2">
          {items.map((p, i) => (
            <motion.article
              key={p.id}
              className="group flex flex-col rounded-2xl border border-white/10 bg-gradient-to-b from-[var(--color-surface-900)] to-[var(--color-surface-950)] p-6 transition hover:border-indigo-500/30"
              initial={reduce ? false : { opacity: 0, y: 16 }}
              whileInView={reduce ? undefined : { opacity: 1, y: 0 }}
              viewport={{ once: true, margin: '-40px' }}
              transition={{ duration: 0.4, delay: i * 0.06 }}
            >
              <div className="mb-3 flex flex-wrap items-center gap-2">
                {p.featured ? (
                  <span className="rounded-full bg-indigo-500/15 px-2.5 py-0.5 text-[10px] font-semibold uppercase tracking-wider text-indigo-300">
                    Featured
                  </span>
                ) : null}
                <span className="text-xs text-slate-500">{p.slug}</span>
              </div>
              <h3 className="font-display text-xl font-semibold text-white">
                {p.title}
              </h3>
              <p className="mt-2 text-sm font-medium text-slate-300">{p.summary}</p>
              {p.description ? (
                <p className="mt-2 text-sm leading-relaxed text-slate-500">{p.description}</p>
              ) : null}
              {p.impact_highlights?.length ? (
                <div className="mt-4">
                  <p className="mb-2 text-[10px] font-semibold uppercase tracking-wider text-indigo-400/90">
                    Impact
                  </p>
                  <ul className="space-y-1.5 text-sm text-slate-400">
                    {p.impact_highlights.map((line) => (
                      <li key={line} className="flex gap-2">
                        <span className="mt-1.5 h-1 w-1 shrink-0 rounded-full bg-indigo-500" />
                        <span>{line}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              ) : null}
              <div className="mt-4 flex flex-wrap gap-2">
                {p.tech_stack?.map((t) => (
                  <span
                    key={t}
                    className="rounded-md border border-white/10 bg-white/5 px-2 py-1 text-xs text-slate-400"
                  >
                    {t}
                  </span>
                ))}
              </div>
              <div className="mt-6 flex flex-wrap gap-3">
                <a
                  href={p.repo_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-sm font-semibold text-indigo-400 transition group-hover:text-indigo-300"
                >
                  GitHub →
                </a>
                {p.demo_url ? (
                  <a
                    href={p.demo_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-sm font-semibold text-slate-400 transition hover:text-white"
                  >
                    Live site →
                  </a>
                ) : null}
              </div>
            </motion.article>
          ))}
        </div>
      )}
    </Section>
  )
}

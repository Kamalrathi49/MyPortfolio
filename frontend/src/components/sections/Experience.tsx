import { motion, useReducedMotion } from 'framer-motion'
import type { ExperienceResponse } from '../../lib/api'
import { Section } from '../ui/Section'

type ExperienceProps = {
  data: ExperienceResponse | null
  loading: boolean
  error: string | null
}

export function Experience({ data, loading, error }: ExperienceProps) {
  const reduce = useReducedMotion()
  const items = data?.items ?? []

  return (
    <Section id="experience" eyebrow="Timeline" title="Experience">
      {loading ? (
        <p className="text-slate-500">Loading experience…</p>
      ) : error ? (
        <p className="text-amber-400/90">{error}</p>
      ) : items.length === 0 ? (
        <p className="text-slate-500">No experience entries yet.</p>
      ) : (
        <div className="space-y-10">
          {items.map((job, i) => (
            <motion.div
              key={job.id}
              className="grid grid-cols-[auto_1fr] gap-5 sm:gap-8"
              initial={reduce ? false : { opacity: 0, y: 12 }}
              whileInView={reduce ? undefined : { opacity: 1, y: 0 }}
              viewport={{ once: true, margin: '-40px' }}
              transition={{ duration: 0.4, delay: i * 0.05 }}
            >
              <div className="flex flex-col items-center pt-1">
                <span className="h-3 w-3 shrink-0 rounded-full bg-indigo-500 ring-4 ring-[var(--color-surface-950)]" />
                {i < items.length - 1 ? (
                  <span className="mt-2 w-px flex-1 min-h-[2.5rem] bg-white/10" />
                ) : null}
              </div>
              <div>
                <p className="text-xs font-semibold uppercase tracking-wider text-indigo-400/90">
                  {job.period}
                </p>
                <h3 className="font-display mt-1 text-lg font-semibold text-white">
                  {job.role}
                </h3>
                <p className="text-sm text-slate-500">{job.company}</p>
                <p className="mt-3 text-sm leading-relaxed text-slate-400">{job.summary}</p>
                <ul className="mt-3 space-y-1.5 text-sm text-slate-500">
                  {job.key_points?.map((h) => (
                    <li key={h} className="flex gap-2">
                      <span className="text-indigo-400">—</span>
                      {h}
                    </li>
                  ))}
                </ul>
              </div>
            </motion.div>
          ))}
        </div>
      )}
    </Section>
  )
}

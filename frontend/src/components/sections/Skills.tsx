import { motion, useReducedMotion } from 'framer-motion'
import type { SkillsResponse } from '../../lib/api'
import { Section } from '../ui/Section'

type SkillsProps = {
  data: SkillsResponse | null
  loading: boolean
  error: string | null
}

export function Skills({ data, loading, error }: SkillsProps) {
  const reduce = useReducedMotion()

  return (
    <Section id="skills" eyebrow="Stack" title="Skills">
      {loading ? (
        <p className="text-slate-500">Loading skills…</p>
      ) : error ? (
        <p className="text-amber-400/90">{error}</p>
      ) : data?.categories?.length ? (
        <div className="grid gap-8 sm:grid-cols-2">
          {data.categories.map((cat, i) => (
            <motion.div
              key={cat.name}
              className="rounded-2xl border border-white/10 bg-[var(--color-surface-900)] p-6"
              initial={reduce ? false : { opacity: 0, y: 14 }}
              whileInView={reduce ? undefined : { opacity: 1, y: 0 }}
              viewport={{ once: true, margin: '-40px' }}
              transition={{ duration: 0.4, delay: i * 0.05 }}
            >
              <h3 className="font-display mb-4 text-lg font-semibold text-white">
                {cat.name}
              </h3>
              <ul className="space-y-4">
                {cat.skills.map((s) => (
                  <li key={s.id}>
                    <div className="flex items-baseline justify-between gap-2">
                      <span className="font-medium text-slate-200">{s.name}</span>
                      <span className="text-xs text-slate-500">
                        {s.years != null ? `${s.years}+ yrs` : ''}
                      </span>
                    </div>
                    <div className="mt-1.5 h-1 overflow-hidden rounded-full bg-white/10">
                      <div
                        className="h-full rounded-full bg-gradient-to-r from-indigo-500 to-violet-400"
                        style={{ width: `${(s.proficiency / 5) * 100}%` }}
                      />
                    </div>
                    {s.highlights?.length ? (
                      <p className="mt-2 text-xs text-slate-500">
                        {s.highlights.join(' · ')}
                      </p>
                    ) : null}
                  </li>
                ))}
              </ul>
            </motion.div>
          ))}
        </div>
      ) : (
        <p className="text-slate-500">No skills published yet.</p>
      )}
    </Section>
  )
}

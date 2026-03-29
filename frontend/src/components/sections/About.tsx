import { motion, useReducedMotion } from 'framer-motion'
import { profile } from '../../data/profile'
import { Section } from '../ui/Section'

export function About() {
  const reduce = useReducedMotion()

  return (
    <Section id="about" eyebrow="About" title="How I work">
      <motion.div
        className="grid gap-10 lg:grid-cols-[1.2fr_1fr]"
        initial={reduce ? false : { opacity: 0, y: 16 }}
        whileInView={reduce ? undefined : { opacity: 1, y: 0 }}
        viewport={{ once: true, margin: '-60px' }}
        transition={{ duration: 0.45 }}
      >
        <div className="space-y-4 text-slate-400 leading-relaxed">
          {profile.aboutLead.map((p) => (
            <p key={p}>{p}</p>
          ))}
          <p className="text-sm text-slate-500">
            Projects, skills, and experience on this site load from{' '}
            <span className="text-slate-300">api.{profile.domain}</span>—OpenAPI-backed,
            same style of contracts I use in production.
          </p>
        </div>
        <ul className="space-y-3 rounded-2xl border border-white/10 bg-[var(--color-surface-900)] p-6 text-sm text-slate-400">
          {profile.aboutBullets.map((line) => (
            <li key={line} className="flex gap-2">
              <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-indigo-400" />
              <span>{line}</span>
            </li>
          ))}
        </ul>
      </motion.div>
    </Section>
  )
}

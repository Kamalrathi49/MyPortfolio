import { motion, useReducedMotion } from 'framer-motion'
import { profile } from '../../data/profile'

export function Hero() {
  const reduce = useReducedMotion()

  return (
    <section
      id="top"
      className="relative overflow-hidden px-4 pb-20 pt-16 sm:px-6 sm:pb-28 sm:pt-24 lg:px-8"
    >
      <div
        className="pointer-events-none absolute inset-0 opacity-40"
        aria-hidden
      >
        <div className="absolute -left-1/4 top-0 h-96 w-96 rounded-full bg-indigo-600/30 blur-3xl" />
        <div className="absolute -right-1/4 bottom-0 h-80 w-80 rounded-full bg-violet-600/20 blur-3xl" />
      </div>
      <div className="relative mx-auto max-w-5xl">
        <motion.p
          className="mb-4 text-xs font-semibold uppercase tracking-[0.25em] text-indigo-400/90"
          initial={reduce ? false : { opacity: 0, y: 8 }}
          animate={reduce ? undefined : { opacity: 1, y: 0 }}
          transition={{ duration: 0.4 }}
        >
          {profile.title}
        </motion.p>
        <motion.h1
          className="font-display text-4xl font-semibold leading-[1.1] tracking-tight text-white sm:text-5xl lg:text-6xl"
          initial={reduce ? false : { opacity: 0, y: 16 }}
          animate={reduce ? undefined : { opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.05 }}
        >
          {profile.name}
        </motion.h1>
        <motion.p
          className="mt-4 max-w-3xl text-lg font-medium leading-snug text-slate-300 sm:text-xl"
          initial={reduce ? false : { opacity: 0, y: 12 }}
          animate={reduce ? undefined : { opacity: 1, y: 0 }}
          transition={{ duration: 0.45, delay: 0.1 }}
        >
          {profile.tagline}
        </motion.p>
        <motion.div
          className="mt-10 flex flex-wrap gap-3"
          initial={reduce ? false : { opacity: 0, y: 16 }}
          animate={reduce ? undefined : { opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.18 }}
        >
          <a
            href="#projects"
            className="inline-flex items-center justify-center rounded-full bg-white px-6 py-3 text-sm font-semibold text-slate-900 transition hover:bg-slate-100"
          >
            View projects
          </a>
          <a
            href="https://api.kamalrathi.dev/docs"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center justify-center rounded-full border border-white/15 bg-white/5 px-6 py-3 text-sm font-semibold text-white backdrop-blur transition hover:border-white/25 hover:bg-white/10"
          >
            API docs
          </a>
        </motion.div>
      </div>
    </section>
  )
}

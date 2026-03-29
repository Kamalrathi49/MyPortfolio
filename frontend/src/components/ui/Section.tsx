import { motion, useReducedMotion } from 'framer-motion'
import type { ReactNode } from 'react'

type SectionProps = {
  id: string
  title: string
  eyebrow?: string
  children: ReactNode
}

export function Section({ id, title, eyebrow, children }: SectionProps) {
  const reduce = useReducedMotion()

  return (
    <section
      id={id}
      className="mx-auto max-w-5xl px-4 py-16 sm:px-6 sm:py-24 lg:px-8"
    >
      <motion.header
        className="mb-10 sm:mb-14"
        initial={reduce ? false : { opacity: 0, y: 12 }}
        whileInView={reduce ? undefined : { opacity: 1, y: 0 }}
        viewport={{ once: true, margin: '-80px' }}
        transition={{ duration: 0.45, ease: [0.22, 1, 0.36, 1] }}
      >
        {eyebrow ? (
          <p className="mb-2 text-xs font-semibold uppercase tracking-[0.2em] text-indigo-400/90">
            {eyebrow}
          </p>
        ) : null}
        <h2 className="font-display text-2xl font-semibold tracking-tight text-white sm:text-3xl">
          {title}
        </h2>
      </motion.header>
      {children}
    </section>
  )
}

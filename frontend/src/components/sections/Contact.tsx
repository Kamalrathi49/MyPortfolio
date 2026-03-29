import { motion, useReducedMotion } from 'framer-motion'
import { useState } from 'react'
import type { FormEvent } from 'react'
import { getErrorMessage, submitContact } from '../../lib/api'
import { Section } from '../ui/Section'

type Status = 'idle' | 'loading' | 'success' | 'error'

export function Contact() {
  const reduce = useReducedMotion()
  const [status, setStatus] = useState<Status>('idle')
  const [message, setMessage] = useState('')
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [subject, setSubject] = useState('')
  const [body, setBody] = useState('')
  const [company, setCompany] = useState('')
  const [honeypot, setHoneypot] = useState('')

  async function onSubmit(e: FormEvent) {
    e.preventDefault()
    setStatus('loading')
    setMessage('')
    try {
      await submitContact({
        name,
        email,
        subject,
        message: body,
        company: company || undefined,
        honeypot: honeypot || undefined,
      })
      setStatus('success')
      setMessage('Thanks — your message is on its way.')
      setName('')
      setEmail('')
      setSubject('')
      setBody('')
      setCompany('')
      setHoneypot('')
    } catch (err) {
      setStatus('error')
      setMessage(getErrorMessage(err, 'Something went wrong. Please try again.'))
    }
  }

  return (
    <Section id="contact" eyebrow="Contact" title="Start a conversation">
      <motion.div
        className="mx-auto max-w-xl"
        initial={reduce ? false : { opacity: 0, y: 12 }}
        whileInView={reduce ? undefined : { opacity: 1, y: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.4 }}
      >
        <p className="mb-8 text-center text-sm text-slate-400">
          Messages are delivered via the API (stored + SMTP). Rate limits apply to
          protect the inbox.
        </p>
        <form
          onSubmit={onSubmit}
          className="space-y-4 rounded-2xl border border-white/10 bg-[var(--color-surface-900)] p-6 sm:p-8"
        >
          <input
            type="text"
            name="company_website"
            value={honeypot}
            onChange={(e) => setHoneypot(e.target.value)}
            className="hidden"
            tabIndex={-1}
            autoComplete="off"
            aria-hidden
          />
          <div>
            <label htmlFor="name" className="mb-1.5 block text-xs font-medium text-slate-400">
              Name
            </label>
            <input
              id="name"
              required
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full rounded-xl border border-white/10 bg-[var(--color-surface-950)] px-4 py-3 text-sm text-white outline-none ring-indigo-500/0 transition focus:border-indigo-500/50 focus:ring-2 focus:ring-indigo-500/30"
            />
          </div>
          <div>
            <label htmlFor="email" className="mb-1.5 block text-xs font-medium text-slate-400">
              Email
            </label>
            <input
              id="email"
              type="email"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full rounded-xl border border-white/10 bg-[var(--color-surface-950)] px-4 py-3 text-sm text-white outline-none focus:border-indigo-500/50 focus:ring-2 focus:ring-indigo-500/30"
            />
          </div>
          <div>
            <label htmlFor="company" className="mb-1.5 block text-xs font-medium text-slate-400">
              Company <span className="text-slate-600">(optional)</span>
            </label>
            <input
              id="company"
              value={company}
              onChange={(e) => setCompany(e.target.value)}
              className="w-full rounded-xl border border-white/10 bg-[var(--color-surface-950)] px-4 py-3 text-sm text-white outline-none focus:border-indigo-500/50 focus:ring-2 focus:ring-indigo-500/30"
            />
          </div>
          <div>
            <label htmlFor="subject" className="mb-1.5 block text-xs font-medium text-slate-400">
              Subject
            </label>
            <input
              id="subject"
              required
              value={subject}
              onChange={(e) => setSubject(e.target.value)}
              className="w-full rounded-xl border border-white/10 bg-[var(--color-surface-950)] px-4 py-3 text-sm text-white outline-none focus:border-indigo-500/50 focus:ring-2 focus:ring-indigo-500/30"
            />
          </div>
          <div>
            <label htmlFor="message" className="mb-1.5 block text-xs font-medium text-slate-400">
              Message
            </label>
            <textarea
              id="message"
              required
              rows={5}
              minLength={10}
              value={body}
              onChange={(e) => setBody(e.target.value)}
              className="w-full resize-y rounded-xl border border-white/10 bg-[var(--color-surface-950)] px-4 py-3 text-sm text-white outline-none focus:border-indigo-500/50 focus:ring-2 focus:ring-indigo-500/30"
            />
          </div>
          {message ? (
            <p
              className={
                status === 'success' ? 'text-sm text-emerald-400' : 'text-sm text-amber-400'
              }
            >
              {message}
            </p>
          ) : null}
          <button
            type="submit"
            disabled={status === 'loading'}
            className="w-full rounded-full bg-indigo-500 py-3.5 text-sm font-semibold text-white shadow-lg shadow-indigo-500/25 transition hover:bg-indigo-400 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {status === 'loading' ? 'Sending…' : 'Send message'}
          </button>
        </form>
      </motion.div>
    </Section>
  )
}

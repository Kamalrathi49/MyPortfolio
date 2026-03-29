import { profile } from '../../data/profile'

const links = [
  { href: '#about', label: 'About' },
  { href: '#skills', label: 'Skills' },
  { href: '#projects', label: 'Projects' },
  { href: '#experience', label: 'Experience' },
  { href: '#contact', label: 'Contact' },
]

export function SiteHeader() {
  return (
    <header className="sticky top-0 z-50 border-b border-white/5 bg-[var(--color-surface-950)]/80 backdrop-blur-md">
      <div className="mx-auto flex max-w-5xl items-center justify-between gap-4 px-4 py-3 sm:px-6 lg:px-8">
        <a
          href="#top"
          className="font-display text-sm font-semibold tracking-tight text-white"
        >
          {profile.domain.replace('.dev', '')}
          <span className="text-indigo-400">.dev</span>
        </a>
        <nav className="hidden items-center gap-6 text-sm text-slate-400 md:flex">
          {links.map((l) => (
            <a
              key={l.href}
              href={l.href}
              className="transition-colors hover:text-white"
            >
              {l.label}
            </a>
          ))}
        </nav>
        <a
          href="#contact"
          className="rounded-full bg-indigo-500 px-4 py-2 text-xs font-semibold text-white shadow-lg shadow-indigo-500/20 transition hover:bg-indigo-400"
        >
          Let&apos;s talk
        </a>
      </div>
    </header>
  )
}

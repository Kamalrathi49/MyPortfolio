import { profile } from '../../data/profile'

export function SiteFooter() {
  return (
    <footer className="border-t border-white/5 py-10 text-center text-sm text-slate-500">
      <p>
        © {new Date().getFullYear()} {profile.name} · FastAPI & React
      </p>
    </footer>
  )
}

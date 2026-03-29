import axios, { AxiosError } from 'axios'

const baseURL =
  import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000'

export const api = axios.create({
  baseURL,
  headers: { 'Content-Type': 'application/json' },
  timeout: 20000,
})

export type ApiErrorBody = {
  error?: {
    code?: string
    message?: string
    request_id?: string
    details?: unknown
  }
}

export function getErrorMessage(err: unknown, fallback: string): string {
  if (axios.isAxiosError(err)) {
    const ax = err as AxiosError<ApiErrorBody>
    const msg = ax.response?.data?.error?.message
    if (typeof msg === 'string' && msg.length > 0) return msg
    if (typeof ax.message === 'string' && ax.message.length > 0) return ax.message
  }
  return fallback
}

export type Project = {
  id: string
  title: string
  slug: string
  summary: string
  description: string | null
  impact_highlights: string[]
  tech_stack: string[]
  repo_url: string
  demo_url: string | null
  featured: boolean
  sort_order: number
  created_at: string
  updated_at: string
}

export type ProjectsResponse = {
  items: Project[]
  total: number
}

export type SkillItem = {
  id: string
  name: string
  proficiency: number
  years: number | null
  highlights: string[]
}

export type SkillCategory = {
  name: string
  skills: SkillItem[]
}

export type SkillsResponse = {
  categories: SkillCategory[]
}

export async function fetchProjects(): Promise<ProjectsResponse> {
  const { data } = await api.get<ProjectsResponse>('/api/v1/projects')
  return data
}

export async function fetchSkills(): Promise<SkillsResponse> {
  const { data } = await api.get<SkillsResponse>('/api/v1/skills')
  return data
}

export type ExperienceItem = {
  id: string
  role: string
  company: string
  period: string
  summary: string
  key_points: string[]
}

export type ExperienceResponse = {
  items: ExperienceItem[]
}

export async function fetchExperience(): Promise<ExperienceResponse> {
  const { data } = await api.get<ExperienceResponse>('/api/v1/experience')
  return data
}

export type ContactPayload = {
  name: string
  email: string
  subject: string
  message: string
  company?: string
  honeypot?: string
}

export async function submitContact(payload: ContactPayload): Promise<{ id: string; status: string }> {
  const { data } = await api.post<{ id: string; status: string }>(
    '/api/v1/contact',
    payload,
  )
  return data
}

export async function recordVisit(path: string): Promise<void> {
  try {
    await api.post('/api/v1/analytics/visit', { path })
  } catch {
    return
  }
}

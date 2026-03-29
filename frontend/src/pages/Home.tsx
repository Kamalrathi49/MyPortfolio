import { useEffect, useState } from 'react'
import { SiteFooter } from '../components/layout/SiteFooter'
import { SiteHeader } from '../components/layout/SiteHeader'
import { About } from '../components/sections/About'
import { Contact } from '../components/sections/Contact'
import { Experience } from '../components/sections/Experience'
import { Hero } from '../components/sections/Hero'
import { Projects } from '../components/sections/Projects'
import { Skills } from '../components/sections/Skills'
import type {
  ExperienceResponse,
  ProjectsResponse,
  SkillsResponse,
} from '../lib/api'
import {
  fetchExperience,
  fetchProjects,
  fetchSkills,
  getErrorMessage,
  recordVisit,
} from '../lib/api'

export function Home() {
  const [projects, setProjects] = useState<ProjectsResponse | null>(null)
  const [projectsLoading, setProjectsLoading] = useState(true)
  const [projectsError, setProjectsError] = useState<string | null>(null)
  const [skills, setSkills] = useState<SkillsResponse | null>(null)
  const [skillsLoading, setSkillsLoading] = useState(true)
  const [skillsError, setSkillsError] = useState<string | null>(null)
  const [experience, setExperience] = useState<ExperienceResponse | null>(null)
  const [experienceLoading, setExperienceLoading] = useState(true)
  const [experienceError, setExperienceError] = useState<string | null>(null)

  useEffect(() => {
    if (typeof sessionStorage !== 'undefined') {
      if (sessionStorage.getItem('portfolio_visit')) return
      sessionStorage.setItem('portfolio_visit', '1')
    }
    void recordVisit('/')
  }, [])

  useEffect(() => {
    let cancelled = false
    ;(async () => {
      try {
        const res = await fetchProjects()
        if (!cancelled) setProjects(res)
      } catch (e) {
        if (!cancelled)
          setProjectsError(getErrorMessage(e, 'Could not load projects.'))
      } finally {
        if (!cancelled) setProjectsLoading(false)
      }
    })()
    return () => {
      cancelled = true
    }
  }, [])

  useEffect(() => {
    let cancelled = false
    ;(async () => {
      try {
        const res = await fetchSkills()
        if (!cancelled) setSkills(res)
      } catch (e) {
        if (!cancelled)
          setSkillsError(getErrorMessage(e, 'Could not load skills.'))
      } finally {
        if (!cancelled) setSkillsLoading(false)
      }
    })()
    return () => {
      cancelled = true
    }
  }, [])

  useEffect(() => {
    let cancelled = false
    ;(async () => {
      try {
        const res = await fetchExperience()
        if (!cancelled) setExperience(res)
      } catch (e) {
        if (!cancelled)
          setExperienceError(getErrorMessage(e, 'Could not load experience.'))
      } finally {
        if (!cancelled) setExperienceLoading(false)
      }
    })()
    return () => {
      cancelled = true
    }
  }, [])

  return (
    <div className="min-h-svh">
      <SiteHeader />
      <main>
        <Hero />
        <About />
        <Skills data={skills} loading={skillsLoading} error={skillsError} />
        <Projects
          data={projects}
          loading={projectsLoading}
          error={projectsError}
        />
        <Experience
          data={experience}
          loading={experienceLoading}
          error={experienceError}
        />
        <Contact />
      </main>
      <SiteFooter />
    </div>
  )
}

'use client'

import { supabase } from '@/lib/supabaseClient'
import { useEffect, useState } from 'react'

export default function Home() {
  const [users, setUsers] = useState<any[]>([])

  useEffect(() => {
    async function loadUsers() {
      const { data, error } = await supabase.from('users').select('*')
      if (error) console.error(error)
      else setUsers(data)
    console.log('Users loaded:', data)
    }

    loadUsers()
  }, [])

  return (
    <div>
      <h1>Table</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>{user.name}</li>
        ))}
        
      </ul>
    </div>
  )
}

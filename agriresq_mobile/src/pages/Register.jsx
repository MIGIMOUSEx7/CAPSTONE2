import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import './Auth.css'

export default function Register() {
  const { register } = useAuth()
  const navigate = useNavigate()
  const [form, setForm] = useState({
    full_name: '', email: '', phone_number: '', password: '', stall_number: '',
  })
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const set = (k, v) => setForm((f) => ({ ...f, [k]: v }))

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)
    try {
      await register(form)
      navigate('/home')
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="auth-page page-no-nav">
      <div className="auth-header">
        <Link to="/" className="back-link">← Back</Link>
        <h2>Create Account</h2>
        <p>Join the AgriResQ marketplace</p>
      </div>
      <form className="auth-form card" onSubmit={handleSubmit}>
        <div className="input-group">
          <label>Full Name</label>
          <input value={form.full_name} onChange={(e) => set('full_name', e.target.value)} required />
        </div>
        <div className="input-group">
          <label>Email</label>
          <input type="email" value={form.email} onChange={(e) => set('email', e.target.value)} required />
        </div>
        <div className="input-group">
          <label>Phone Number</label>
          <input type="tel" value={form.phone_number} onChange={(e) => set('phone_number', e.target.value)} placeholder="09XX XXX XXXX" />
        </div>
        <div className="input-group">
          <label>Password</label>
          <input type="password" value={form.password} onChange={(e) => set('password', e.target.value)} required minLength={8} />
        </div>
        <div className="input-group">
          <label>Stall Number (optional)</label>
          <input
            value={form.stall_number}
            onChange={(e) => set('stall_number', e.target.value)}
            placeholder="e.g. Stall 1"
          />
          <small style={{ color: 'var(--gray-600)', marginTop: '6px', display: 'block' }}>
            Provide a stall number to register as a stall operator. Leave blank to register as a rescue buyer.
          </small>
        </div>
        {error && <p className="error-text">{error}</p>}
        <button type="submit" className="btn btn-green" disabled={loading}>
          {loading ? 'Creating...' : 'Create Account'}
        </button>
        <p className="auth-footer">
          Already have an account? <Link to="/login">Sign In</Link>
        </p>
      </form>
    </div>
  )
}

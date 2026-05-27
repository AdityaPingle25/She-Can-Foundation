const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, '')));

const SUBMISSIONS_FILE = path.join(__dirname, 'data', 'submissions.json');

// Ensure submissions file exists
if (!fs.existsSync(SUBMISSIONS_FILE)) {
  fs.writeFileSync(SUBMISSIONS_FILE, JSON.stringify([]));
}

// ----------------------------------------------------
// API ROUTES
// ----------------------------------------------------

// POST /api/volunteer - Submit a new application
app.post('/api/volunteer', (req, res) => {
  const { name, email } = req.body;
  if (!name || !email) {
    return res.status(400).json({ error: 'Name and email are required.' });
  }

  const submissions = JSON.parse(fs.readFileSync(SUBMISSIONS_FILE));
  const newSubmission = {
    id: Date.now(),
    name,
    email,
    date: new Date().toISOString()
  };

  submissions.push(newSubmission);
  fs.writeFileSync(SUBMISSIONS_FILE, JSON.stringify(submissions, null, 2));

  res.status(201).json({ success: true, message: 'Application submitted successfully!', data: newSubmission });
});



// Mock Chatbot API Endpoint
app.post('/api/chat', (req, res) => {
  const { message } = req.body;
  const lower = message.toLowerCase();
  
  let reply = "Thank you for reaching out to She Can Foundation. How else can I assist you today?";
  
  if (lower.includes('donate') || lower.includes('money')) {
    reply = "Every contribution counts! 100% of your donation goes directly towards our ground operations. You can donate securely via our <a href='donate.html' style='color:var(--rose); text-decoration:underline;'>Donate page</a>. ₹1500 provides dignity kits to 15 girls for an entire month.";
  } else if (lower.includes('volunteer') || lower.includes('join')) {
    reply = "We're thrilled you want to join us! You can volunteer by clicking the 'Volunteer' button on the homepage and filling out the quick form.";
  } else if (lower.includes('location') || lower.includes('located') || lower.includes('where')) {
    reply = "Our NGO operates across 250+ villages in India, with our registered office in New Delhi.";
  } else if (lower.includes('certificate') || lower.includes('registered')) {
    reply = "We are fully registered under the Indian Society Act, 1860. You can view our official registration on the 'Our Certificate' page.";
  } else if (lower.includes('hello') || lower.includes('hi')) {
    reply = "Hello! I'm the She Can AI Assistant. I can help answer questions about volunteering, donating, or our foundation's mission.";
  }

  // Simulate network delay for realism
  setTimeout(() => {
    res.json({ reply });
  }, 1000); // Simulate network delay
});

// ----------------------------------------------------
// START SERVER
// ----------------------------------------------------
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});

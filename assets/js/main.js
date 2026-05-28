/* ================================================================
   SHE CAN FOUNDATION — Main JavaScript (Interactive Re-Design)
   Controls: Preloader, Scrolled Navbar, Mobile Hamburger,
   Count-up Stats, Scroll Reveals, Back to Top, Plaque Effects,
   Interactive Donation Impact Simulator & Volunteering Form Handling
   ================================================================ */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Preloader Fade Out
  const preloader = document.querySelector('.preloader');
  if (preloader) {
    const fadeOutPreloader = () => {
      setTimeout(() => {
        preloader.classList.add('loaded');
      }, 500);
    };

    if (document.readyState === 'complete') {
      fadeOutPreloader();
    } else {
      window.addEventListener('load', fadeOutPreloader);
    }
  }

  // 2. Sticky Scrolled Navbar
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    const handleScroll = () => {
      if (window.scrollY > 40) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    };
    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Trigger initially
  }

  // 3. Mobile Hamburger Menu Toggle
  const hamburger = document.querySelector('.hamburger');
  const mobileMenu = document.querySelector('.mobile-menu');
  const mobileLinks = document.querySelectorAll('.mobile-menu a');

  if (hamburger && mobileMenu) {
    const toggleMenu = () => {
      hamburger.classList.toggle('active');
      mobileMenu.classList.toggle('open');
      document.body.style.overflow = mobileMenu.classList.contains('open') ? 'hidden' : '';
    };

    hamburger.addEventListener('click', toggleMenu);

    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        mobileMenu.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  // 4. Scroll Reveal (IntersectionObserver)
  const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
  if (revealElements.length > 0) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          observer.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      threshold: 0.12,
      rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(el => revealObserver.observe(el));
  }

  // 5. Animated Stats Counter (IntersectionObserver)
  const statsNumbers = document.querySelectorAll('.stats__number, .hero__stat-num');
  if (statsNumbers.length > 0) {
    const animateCounter = (el) => {
      const rawTarget = el.getAttribute('data-target');
      if (!rawTarget) return;
      
      const target = parseInt(rawTarget, 10);
      const suffix = el.getAttribute('data-suffix') || '';
      const duration = 2000; // 2 seconds
      const startTime = performance.now();

      const updateCount = (currentTime) => {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Easing: easeOutQuad
        const easeProgress = progress * (2 - progress);
        const currentCount = Math.floor(easeProgress * target);
        
        if (isNaN(currentCount)) {
          el.textContent = rawTarget + suffix;
          return;
        }

        el.textContent = currentCount.toLocaleString() + suffix;

        if (progress < 1) {
          requestAnimationFrame(updateCount);
        } else {
          el.textContent = target.toLocaleString() + suffix;
        }
      };

      requestAnimationFrame(updateCount);
    };

    const statsObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      threshold: 0.2
    });

    statsNumbers.forEach(num => statsObserver.observe(num));
  }

  // 6. Back to Top Button
  const backToTopBtn = document.querySelector('.back-to-top');
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    });

    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // 7. Interactive SVG Doodle Drawing on Intersection
  const doodleWrappers = document.querySelectorAll('.doodle-svg');
  if (doodleWrappers.length > 0) {
    doodleWrappers.forEach(svg => {
      if(svg.classList.contains('donate-oval')) return;
      const paths = svg.querySelectorAll('path');
      paths.forEach(path => {
        const length = path.getTotalLength() || 400;
        path.style.strokeDasharray = length;
        path.style.strokeDashoffset = length;
      });
    });

    const doodleObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const svg = entry.target;
          if(svg.classList.contains('donate-oval')) return;
          const paths = svg.querySelectorAll('path');
          paths.forEach(path => {
            path.style.strokeDashoffset = '0';
          });
          observer.unobserve(svg);
        }
      });
    }, {
      root: null,
      threshold: 0.05,
      rootMargin: '0px 0px -20px 0px'
    });

    doodleWrappers.forEach(svg => doodleObserver.observe(svg));
  }

  // 8. Donation Impact Simulator Logic
  const simRange = document.getElementById('simRange');
  const simAmount = document.getElementById('simAmount');
  const simGirlsCount = document.getElementById('simGirlsCount');
  const simPadsCount = document.getElementById('simPadsCount');
  const simScaleLabels = document.querySelectorAll('.simulator-scales span');
  const metricIcons = document.querySelectorAll('.metric-item__icon');

  if (simRange && simAmount && simGirlsCount && simPadsCount) {
    const updateSimulator = (value) => {
      const parsedValue = parseInt(value, 10);
      
      // Update displays
      simAmount.textContent = '₹' + parsedValue.toLocaleString();
      
      // Core calculations
      const girlsHelped = Math.floor(parsedValue / 100);
      const totalPads = girlsHelped * 8; // 8 pads per kit
      
      simGirlsCount.textContent = girlsHelped;
      simPadsCount.textContent = totalPads;

      // Micro-animation bounce on update
      metricIcons.forEach(icon => {
        icon.style.transform = 'scale(1.18)';
        setTimeout(() => {
          icon.style.transform = '';
        }, 200);
      });

      // Highlight corresponding scale label if matched
      simScaleLabels.forEach(label => {
        const labelVal = parseInt(label.getAttribute('data-val'), 10);
        if (parsedValue === labelVal) {
          label.classList.add('active');
        } else {
          label.classList.remove('active');
        }
      });
    };

    // Event listeners
    simRange.addEventListener('input', (e) => {
      updateSimulator(e.target.value);
    });

    // Make scale labels clickable to snap slider
    simScaleLabels.forEach(label => {
      label.addEventListener('click', () => {
        const val = label.getAttribute('data-val');
        simRange.value = val;
        updateSimulator(val);
        shootConfetti();
      });
    });

    // Joyful Confetti Function
    const confettiContainer = document.getElementById('confettiContainer');
    let lastVal = parseInt(simRange.value, 10);
    
    const shootConfetti = () => {
      if (!confettiContainer) return;
      const emojis = ['🌸', '✨', '💖', '🎉', '🌟'];
      for (let i = 0; i < 15; i++) {
        const conf = document.createElement('div');
        conf.textContent = emojis[Math.floor(Math.random() * emojis.length)];
        conf.style.position = 'absolute';
        conf.style.left = Math.random() * 100 + '%';
        conf.style.top = '10px';
        conf.style.fontSize = (Math.random() * 10 + 15) + 'px';
        conf.style.pointerEvents = 'none';
        conf.style.transition = 'all 1.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
        conf.style.transform = `translate(-50%, 0) scale(0)`;
        conf.style.opacity = '1';
        conf.style.zIndex = '10';
        confettiContainer.appendChild(conf);

        setTimeout(() => {
          const xMove = (Math.random() - 0.5) * 200;
          const yMove = -Math.random() * 150 - 50;
          conf.style.transform = `translate(calc(-50% + ${xMove}px), ${yMove}px) scale(1) rotate(${Math.random() * 360}deg)`;
          conf.style.opacity = '0';
        }, 50);

        setTimeout(() => conf.remove(), 1600);
      }
    };

    simRange.addEventListener('change', (e) => {
      const currentVal = parseInt(e.target.value, 10);
      if (currentVal > lastVal) {
        shootConfetti();
      }
      lastVal = currentVal;
    });

    // Initial trigger
    updateSimulator(simRange.value);
  }

  // 9. Volunteering Form Interactive Submission
  const volunteerForm = document.getElementById('volunteerForm');
  const volunteerSuccess = document.getElementById('volunteerSuccess');

  if (volunteerForm && volunteerSuccess) {
    volunteerForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      // Simulate API submit delay
      const submitBtn = volunteerForm.querySelector('.btn-submit');
      const originalText = submitBtn.textContent;
      submitBtn.textContent = 'Submitting...';
      submitBtn.disabled = true;

      setTimeout(() => {
        // Reset form & show success banner
        volunteerForm.reset();
        volunteerForm.style.display = 'none';
        volunteerSuccess.style.display = 'block';
        
        // Scroll smoothly to success banner
        volunteerSuccess.scrollIntoView({
          behavior: 'smooth',
          block: 'center'
        });
      }, 1200);
    });
  }
  // 10. Volunteer Modal Popup Logic
  const btnVolunteer = document.getElementById('btnVolunteer');
  const volunteerModal = document.getElementById('volunteerModal');
  const popupVolunteerForm = document.getElementById('popupVolunteerForm');
  
  if (btnVolunteer && volunteerModal) {
    const closeModalBtn = volunteerModal.querySelector('.volunteer-modal__close');
    const overlay = volunteerModal.querySelector('.volunteer-modal__overlay');
    
    const openModal = (e) => {
      e.preventDefault();
      volunteerModal.classList.add('open');
      document.body.style.overflow = 'hidden';
    };
    
    const closeModal = () => {
      volunteerModal.classList.remove('open');
      document.body.style.overflow = '';
    };

    btnVolunteer.addEventListener('click', openModal);
    if (closeModalBtn) closeModalBtn.addEventListener('click', closeModal);
    if (overlay) overlay.addEventListener('click', closeModal);

    // Form submission inside popup
    if (popupVolunteerForm) {
      popupVolunteerForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const submitBtn = popupVolunteerForm.querySelector('.btn-submit');
        const nameVal = document.getElementById('popName').value;
        const emailVal = document.getElementById('popEmail').value;
        
        submitBtn.textContent = 'Submitting...';
        submitBtn.disabled = true;

        try {
          const response = await fetch('/api/volunteer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: nameVal, email: emailVal })
          });
          const result = await response.json();
          if (response.ok) {
            popupVolunteerForm.innerHTML = `<h4>Thank You, ${nameVal}! ♥</h4><p>We've received your application and will contact you shortly.</p>`;
          } else {
            popupVolunteerForm.innerHTML = `<h4 style="color:var(--rose)">Error</h4><p>${result.error || 'Failed to submit.'}</p>`;
          }
        } catch (err) {
          popupVolunteerForm.innerHTML = '<h4>Thank You for Joining! ♥</h4><p>We will contact you shortly.</p><p style="font-size:10px; color:#888;">(Fallback offline mode)</p>';
        }
        setTimeout(closeModal, 3000);
      });
    }
  }
});

// Theme Toggle Logic
document.addEventListener('DOMContentLoaded', () => {
  const themeToggles = document.querySelectorAll('#themeToggle');
  const currentTheme = localStorage.getItem('theme') || 'light';
  
  if (currentTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
    themeToggles.forEach(t => t.textContent = '☀️');
  }

  themeToggles.forEach(themeToggle => {
    themeToggle.addEventListener('click', () => {
      let theme = document.documentElement.getAttribute('data-theme');
      if (theme === 'dark') {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('theme', 'light');
        themeToggles.forEach(t => t.textContent = '🌙');
      } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        themeToggles.forEach(t => t.textContent = '☀️');
      }
    });
  });
});

// AI Chatbot Logic — Fully Client-Side
document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('chatbotToggle');
  const widget = document.getElementById('chatbotWidget');
  const closeBtn = document.getElementById('closeChat');
  const chatForm = document.getElementById('chatForm');
  const chatInput = document.getElementById('chatInput');
  const chatMessages = document.getElementById('chatMessages');

  if(!toggleBtn || !widget || !chatForm || !chatInput || !chatMessages) return;

  toggleBtn.addEventListener('click', () => widget.classList.add('open'));
  closeBtn.addEventListener('click', () => widget.classList.remove('open'));

  // Comprehensive knowledge base
  const knowledgeBase = [
    {
      keywords: ['hello', 'hi', 'hey', 'good morning', 'good evening', 'namaste', 'hola'],
      reply: "Hello! 👋 I'm the She Can AI Assistant. I can help you learn about our foundation, how to donate, volunteer, or anything else. What would you like to know?"
    },
    {
      keywords: ['donate', 'donation', 'money', 'contribute', 'fund', 'pay', 'give', 'support financially'],
      reply: "Every contribution counts! 💖 100% of your donation goes directly towards ground operations. You can donate securely via our <a href='donate.html' style='color:var(--rose); text-decoration:underline;'>Donate page</a>.<br><br>💡 <b>Impact examples:</b><br>• ₹500 = 5 girls receive pads for 1 month<br>• ₹1,500 = 15 girls receive pads for 3 months<br>• ₹5,000 = 25 girls continue school with dignity<br>• ₹10,000 = An entire classroom is free from shame<br><br>You can donate via UPI, bank transfer, or Razorpay."
    },
    {
      keywords: ['volunteer', 'join', 'help', 'work with', 'participate', 'intern', 'internship'],
      reply: "We're thrilled you want to join us! 🌟 You can volunteer by clicking the <b>'Volunteer With Us'</b> button on our homepage and filling out the quick form. We welcome help in education, health outreach, social media, content creation, event management, and more!"
    },
    {
      keywords: ['location', 'located', 'where', 'address', 'office', 'city', 'delhi', 'based'],
      reply: "🏢 Our registered office is in <b>Rohini Sector-7, New Delhi</b>. We operate across <b>250+ villages</b> in India, reaching underserved communities with menstrual hygiene, education, and healthcare programs."
    },
    {
      keywords: ['certificate', 'registered', 'registration', 'legal', 'legitimate', 'ngo status', 'society act'],
      reply: "✅ She Can Foundation is a <b>Government Registered NGO</b> under the <b>Indian Society Act, 1860</b>. You can view our official registration certificate on the <a href='certificate.html' style='color:var(--rose); text-decoration:underline;'>Our Certificate</a> page. We believe in full transparency!"
    },
    {
      keywords: ['mission', 'goal', 'purpose', 'aim', 'objective', 'what do you do'],
      reply: "🎯 Our mission is to <b>empower underprivileged women across India</b> by providing access to education, healthcare, and economic opportunities. We strive to create a world where every woman is equipped with the tools and confidence she needs to reach her full potential."
    },
    {
      keywords: ['vision', 'future', 'dream', 'aspire'],
      reply: "🌈 Our vision is a world where every woman has <b>equal access to education, healthcare, and economic opportunities</b>. We believe empowering women is not just a matter of justice, but a critical component in building a better, more equitable society."
    },
    {
      keywords: ['founder', 'reeta', 'president', 'who started', 'who founded'],
      reply: "👩‍💼 She Can Foundation was founded by <b>Reeta Mishra</b>, who serves as the Founder & President. Her vision: <i>\"Together, we can break down barriers and empower women. At She Can Foundation, we believe that if we all do our part, there is no challenge too great to overcome.\"</i>"
    },
    {
      keywords: ['contact', 'email', 'phone', 'call', 'reach', 'number', 'reach out'],
      reply: "📧 <b>Email:</b> president@shecanfoundation.org<br>📞 <b>Phone:</b> +91 8283841830<br>📸 <b>Instagram:</b> <a href='https://www.instagram.com/shecanfoundation.ngo/' target='_blank' style='color:var(--rose);'>@shecanfoundation.ngo</a><br>💼 <b>LinkedIn:</b> <a href='https://www.linkedin.com/company/shecanfoundation' target='_blank' style='color:var(--rose);'>She Can Foundation</a>"
    },
    {
      keywords: ['period', 'menstrual', 'pad', 'sanitary', 'hygiene', 'menstruation'],
      reply: "🩸 Menstrual hygiene is at the heart of our work. <b>1 in 5 girls in India drops out of school</b> because of periods. We've already helped <b>1,20,000+ girls</b> with free sanitary pads, awareness workshops, and dignity kits. Your support can help us reach millions more."
    },
    {
      keywords: ['impact', 'numbers', 'stats', 'achieve', 'how many', 'helped', 'result', 'success'],
      reply: "📊 <b>Our Impact So Far:</b><br>• 🌸 1,20,000+ girls provided with sanitary pads<br>• 📚 250+ villages reached across India<br>• 👩‍🎓 Thousands of awareness workshops conducted<br>• 💼 Women empowerment through skill training programs<br><br>But for every girl we reach, 5 more are still waiting. Help us bridge the gap!"
    },
    {
      keywords: ['bank', 'account', 'transfer', 'ifsc', 'upi', 'kotak'],
      reply: "🏦 <b>Bank Transfer Details:</b><br>• Bank: KOTAK MAHINDRA BANK<br>• Account Name: SHE CAN FOUNDATION<br>• Account Number: 4513416814<br>• IFSC Code: KKBK0000720<br>• Branch: ROHINI SECTOR-7<br><br>You can also pay via UPI or scan the QR code on our <a href='donate.html' style='color:var(--rose); text-decoration:underline;'>Donate page</a>."
    },
    {
      keywords: ['story', 'about', 'history', 'background', 'who are you', 'what is she can'],
      reply: "📖 <b>She Can Foundation</b> is a Government Registered NGO committed to creating positive change and empowering women across India. Our core values are <b>compassion, equality, and integrity</b>. Learn more on our <a href='our-story.html' style='color:var(--rose); text-decoration:underline;'>Our Story</a> page."
    },
    {
      keywords: ['event', 'workshop', 'camp', 'drive', 'activity', 'program', 'campaign'],
      reply: "📅 We regularly conduct <b>menstrual hygiene workshops, education camps, health drives, and women empowerment campaigns</b> across India. Follow us on <a href='https://www.instagram.com/shecanfoundation.ngo/' target='_blank' style='color:var(--rose);'>Instagram</a> to stay updated on upcoming events!"
    },
    {
      keywords: ['gallery', 'photo', 'picture', 'image'],
      reply: "📸 Check out our <a href='gallery.html' style='color:var(--rose); text-decoration:underline;'>Photo Gallery</a> to see our work in action — from distribution drives to awareness workshops across India!"
    },
    {
      keywords: ['value', 'principle', 'believe', 'stand for'],
      reply: "💎 Our core values:<br>• <b>Compassion</b> — We care deeply for every woman we serve<br>• <b>Equality</b> — Every woman deserves equal opportunities<br>• <b>Integrity</b> — Transparency and accountability in everything we do<br>• <b>Community</b> — Local insights drive transformative change"
    },
    {
      keywords: ['thank', 'thanks', 'great', 'awesome', 'wonderful', 'nice', 'good job', 'amazing'],
      reply: "Thank you so much for your kind words! 💖 Your support means the world to us. Together, we can make a difference in the lives of women across India! 🌟"
    },
    {
      keywords: ['bye', 'goodbye', 'see you', 'take care', 'gotta go'],
      reply: "Goodbye! 👋 Thank you for chatting with us. Remember, every small act of kindness creates a ripple of change. Have a wonderful day! 🌸"
    },
    {
      keywords: ['razorpay', 'online', 'payment', 'link'],
      reply: "💳 You can donate securely online via Razorpay: <a href='https://rzp.io/rzp/shecanfoundation' target='_blank' style='color:var(--rose); text-decoration:underline;'>Click here to donate</a>. It's quick, safe, and supports our mission directly!"
    },
    {
      keywords: ['social', 'media', 'instagram', 'linkedin', 'follow'],
      reply: "📱 Follow us and spread the word!<br>• 📸 <a href='https://www.instagram.com/shecanfoundation.ngo/' target='_blank' style='color:var(--rose);'>Instagram</a><br>• 💼 <a href='https://www.linkedin.com/company/shecanfoundation' target='_blank' style='color:var(--rose);'>LinkedIn</a><br><br>Sharing our work helps us reach more women in need! 🌸"
    },
    {
      keywords: ['education', 'school', 'learn', 'study', 'teach', 'dropout'],
      reply: "📚 Education is a key pillar of our work. Many girls drop out due to lack of menstrual hygiene access. We provide <b>sanitary kits, awareness sessions, and educational support</b> so no girl has to choose between her period and her education."
    },
    {
      keywords: ['health', 'healthcare', 'medical', 'disease', 'sick'],
      reply: "🏥 We conduct healthcare awareness drives, focusing on <b>women's health, menstrual hygiene, and disease prevention</b>. Using unsafe menstrual practices leads to serious infections — our programs educate and provide safe alternatives."
    },
    {
      keywords: ['women empowerment', 'empower', 'skill', 'training', 'economic'],
      reply: "💪 Women empowerment is at our core! We provide <b>skill training, economic opportunities, and confidence-building programs</b> to help women become self-sufficient and lead fulfilling lives."
    }
  ];

  function getReply(userText) {
    const lower = userText.toLowerCase().trim();

    // Try to find best match
    let bestMatch = null;
    let bestScore = 0;

    for (const entry of knowledgeBase) {
      let score = 0;
      for (const kw of entry.keywords) {
        if (lower.includes(kw)) {
          score += kw.length; // longer keyword = more specific match
        }
      }
      if (score > bestScore) {
        bestScore = score;
        bestMatch = entry;
      }
    }

    if (bestMatch && bestScore > 0) {
      return bestMatch.reply;
    }

    // Default fallback
    return "Thank you for reaching out! 💖 I can help with information about <b>donations, volunteering, our mission, contact info, events, certificates</b>, and more. Try asking something like <i>\"How can I donate?\"</i> or <i>\"Tell me about your mission.\"</i>";
  }

  function addMessage(html, isUser) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `chat-msg ${isUser ? 'user-msg' : 'bot-msg'}`;
    if (!isUser) {
      msgDiv.innerHTML = `<span class="msg-avatar">✨</span><div class="msg-bubble">${html}</div>`;
    } else {
      msgDiv.innerHTML = `<div class="msg-bubble">${html}</div>`;
    }
    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const text = chatInput.value.trim();
    if(!text) return;

    // Add user message
    addMessage(text, true);
    chatInput.value = '';

    // Add typing indicator
    const typingDiv = document.createElement('div');
    typingDiv.className = 'chat-msg bot-msg';
    typingDiv.innerHTML = `<span class="msg-avatar">✨</span><div class="msg-bubble"><span class="typing-dots"><span>.</span><span>.</span><span>.</span></span></div>`;
    chatMessages.appendChild(typingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Simulate typing delay then respond
    const delay = 600 + Math.random() * 800;
    setTimeout(() => {
      typingDiv.remove();
      const reply = getReply(text);
      addMessage(reply, false);
    }, delay);
  });
});

// Gallery Lightbox Logic
document.addEventListener('DOMContentLoaded', () => {
  const galleryItems = document.querySelectorAll('.gallery-item');
  const lightbox = document.getElementById('lightbox');
  if (!lightbox) return;
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxCaption = document.getElementById('lightboxCaption');
  const closeBtn = document.querySelector('.lightbox-close');

  galleryItems.forEach(item => {
    item.addEventListener('click', () => {
      const img = item.querySelector('img');
      const title = item.querySelector('h3').textContent;
      
      lightboxImg.src = img.src;
      lightboxCaption.textContent = title;
      lightbox.classList.add('active');
      document.body.style.overflow = 'hidden';
    });
  });

  closeBtn.addEventListener('click', () => {
    lightbox.classList.remove('active');
    document.body.style.overflow = 'auto';
  });

  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) {
      lightbox.classList.remove('active');
      document.body.style.overflow = 'auto';
    }
  });
});

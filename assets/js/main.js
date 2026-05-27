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

// AI Chatbot Logic
document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('chatbotToggle');
  const widget = document.getElementById('chatbotWidget');
  const closeBtn = document.getElementById('closeChat');
  const chatForm = document.getElementById('chatForm');
  const chatInput = document.getElementById('chatInput');
  const chatMessages = document.getElementById('chatMessages');

  if(toggleBtn && widget) {
    toggleBtn.addEventListener('click', () => widget.classList.add('open'));
    closeBtn.addEventListener('click', () => widget.classList.remove('open'));

    chatForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const text = chatInput.value.trim();
      if(!text) return;

      // Add user message
      chatMessages.innerHTML += `<div class="chat-msg user-msg"><div class="msg-bubble">${text}</div></div>`;
      chatInput.value = '';
      chatMessages.scrollTop = chatMessages.scrollHeight;

      // Add typing indicator
      const typingId = 'typing-' + Date.now();
      chatMessages.innerHTML += `<div id="${typingId}" class="chat-msg bot-msg"><span class="msg-avatar">✨</span><div class="msg-bubble">...</div></div>`;
      chatMessages.scrollTop = chatMessages.scrollHeight;

      try {
        const response = await fetch('/api/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message: text })
        });
        if (!response.ok) throw new Error("API Offline");
        const data = await response.json();
        document.getElementById(typingId).remove();
        chatMessages.innerHTML += `<div class="chat-msg bot-msg"><span class="msg-avatar">✨</span><div class="msg-bubble">${data.reply}</div></div>`;
      } catch(err) {
        document.getElementById(typingId).remove();
        let fallback = "Thank you for reaching out to She Can Foundation! How else can I assist you today?";
        const lower = text.toLowerCase();
        if (lower.includes('donate') || lower.includes('money')) {
          fallback = "Every contribution counts! 100% of your donation goes directly towards our ground operations. You can donate securely via our Donate page.";
        } else if (lower.includes('volunteer') || lower.includes('join')) {
          fallback = "We're thrilled you want to join us! Please click the 'Volunteer With Us' button on our homepage.";
        }
        chatMessages.innerHTML += `<div class="chat-msg bot-msg"><span class="msg-avatar">✨</span><div class="msg-bubble">${fallback}</div></div>`;
      }
      chatMessages.scrollTop = chatMessages.scrollHeight;
    });
  }
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

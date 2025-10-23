# Compliment Generator Training Wheels - User Stories

## Core User Personas

**Sarah** - 28, software engineer, socially anxious, wants to be a better teammate but freezes when trying to give genuine praise

**Marcus** - 35, manager, gives generic compliments ("good job!"), wants to motivate his team more effectively

**Jen** - 22, college student, struggles with making deeper friendships, compliments feel forced or fake when she tries

---

## Epic 1: Getting Started & Onboarding

### User Story 1.1: First Time Setup
**As a** new user  
**I want to** understand what this app does and why it matters  
**So that** I'm motivated to improve my compliment skills

**Acceptance Criteria:**
- Welcome screen explains the "why" - how genuine compliments strengthen relationships
- Quick assessment: "How comfortable are you giving compliments?" (scale 1-5)
- User selects contexts they want to improve in: Work, Friends, Family, Dating, Strangers
- Option to skip tutorial or take guided tour
- Takes less than 2 minutes to complete

**UI Notes:**
- Warm, encouraging tone (not preachy or therapeutic)
- Illustrations showing awkward vs. smooth compliment scenarios
- Progress dots showing 3-step setup

---

### User Story 1.2: Understanding My Patterns
**As a** user  
**I want to** see examples of bad vs. good compliments  
**So that** I understand what I'm working toward

**Acceptance Criteria:**
- Show side-by-side comparisons:
  - ❌ "Good job on the presentation"
  - ✅ "The way you explained that complex data in simple terms really helped everyone understand"
- Interactive quiz: User rates 5 compliments as Generic/Specific/Too Much
- Immediate feedback on quiz responses
- Unlocks first "compliment mission"

---

## Epic 2: Daily Practice & Coaching

### User Story 2.1: Context-Aware Suggestions
**As a** user in a specific social situation  
**I want to** get relevant compliment ideas  
**So that** I don't sound robotic or out-of-place

**Acceptance Criteria:**
- Home screen has context buttons: "At Work," "With Friends," "Family," "Date," "Random Encounter"
- Selecting context shows 3-5 compliment frameworks:
  - "I noticed you..." (observation-based)
  - "I appreciate when you..." (behavior-based)
  - "You're really good at..." (skill-based)
- Each framework has 2-3 fill-in-the-blank examples
- Option to save favorites
- "Generate Another" button for more ideas

**Example Flow:**
1. Sarah selects "At Work"
2. App suggests: "I noticed you [stayed late to help with the bug] - that really [saved the release]. I appreciate that."
3. Sarah can customize the bracketed parts
4. Sarah taps "This helped!" or "Not quite right"

---

### User Story 2.2: Real-Time Compliment Coach
**As a** user crafting my own compliment  
**I want to** get instant feedback  
**So that** I can improve before actually saying it

**Acceptance Criteria:**
- Text input field: "What do you want to say?"
- Real-time analysis shows:
  - ✅ Specificity score (1-5 stars)
  - ✅ Sincerity indicator (checks for generic phrases)
  - ⚠️ Warning if too effusive/over-the-top
  - 💡 Suggestions to make it better
- Tap suggestion to auto-improve the text
- "Looks good!" confirmation when ready
- Option to save or share

**Example:**
- Marcus types: "Good work on the report"
- App responds: "⭐⭐ - Try being more specific! What exactly was good?"
- Marcus adds: "Good work on the report - the visualizations made the trends really clear"
- App responds: "⭐⭐⭐⭐ - Much better! This is specific and actionable."

---

### User Story 2.3: Practice Mode
**As a** user wanting to build confidence  
**I want to** practice without real consequences  
**So that** I can experiment and learn

**Acceptance Criteria:**
- "Practice Scenarios" section with role-play situations:
  - Coworker did something helpful
  - Friend showed up for you emotionally
  - Partner cooked dinner
  - Stranger held the door
- User types their compliment attempt
- AI responds as the recipient (text simulation)
- Shows if compliment landed well or felt awkward
- Offers coaching: "Good start! Try adding why this mattered to you..."
- Can replay scenarios multiple times

---

## Epic 3: Tracking & Motivation

### User Story 3.1: Compliment Streak
**As a** user building a habit  
**I want to** see my progress  
**So that** I stay motivated

**Acceptance Criteria:**
- Home screen shows current streak: "🔥 5 days of genuine compliments!"
- Calendar view with completed days marked
- Goal: Give at least 1 quality compliment per day
- Streak breaks if no compliments logged for 24 hours
- Push notification reminder: "Have you brightened someone's day today?"
- Celebrates milestones: 7 days, 30 days, 100 days

---

### User Story 3.2: Impact Journal
**As a** user  
**I want to** remember the compliments I've given  
**So that** I can see my growth and feel good about spreading positivity

**Acceptance Criteria:**
- Journal tab shows all logged compliments
- Entries include:
  - Date/time
  - Context (work/friend/family)
  - The compliment text
  - Optional note: "How did they react?"
  - Mood/emoji before and after giving it
- Filter by context, date range
- Stats dashboard:
  - Total compliments given
  - Most common context
  - Specificity trend over time
- Export option (PDF or text)

---

### User Story 3.3: Level Up System
**As a** user  
**I want to** unlock achievements  
**So that** learning feels game-like and fun

**Acceptance Criteria:**
- User has a "Compliment Level" (1-10)
- XP earned for:
  - Daily compliment logged (+10 XP)
  - High specificity score (+5 bonus XP)
  - Completing practice scenarios (+15 XP)
  - Week-long streak (+50 XP)
- Badges unlocked:
  - "First Steps" (1st compliment)
  - "Streak Starter" (7 days)
  - "Specificity Master" (10 compliments rated 4+ stars)
  - "Conversation Catalyst" (50 total compliments)
- Each level unlock shows new tips/advanced techniques

---

## Epic 4: Advanced Features

### User Story 4.1: Compliment Library
**As a** user  
**I want to** browse examples organized by situation  
**So that** I can learn from diverse scenarios

**Acceptance Criteria:**
- Searchable database of compliments
- Categories:
  - Professional (presentations, teamwork, leadership)
  - Personal (appearance, personality, actions)
  - Creative (art, writing, cooking)
  - Emotional support (empathy, listening)
- Each example labeled: Specific, Sincere, Actionable
- User can favorite examples
- Community submissions (moderated)

---

### User Story 4.2: Conversation Starter Integration
**As a** user in an awkward silence  
**I want to** transition from small talk to meaningful conversation  
**So that** I can deepen relationships

**Acceptance Criteria:**
- "Icebreaker Mode" button
- Suggests questions that could lead to compliment opportunities:
  - "What's something you're proud of lately?"
  - "What's a skill you wish more people noticed about you?"
- After they answer, app suggests compliment based on their response
- Teaches the flow: Ask → Listen → Compliment

---

### User Story 4.3: Reminder Campaigns
**As a** user who forgets to practice  
**I want to** gentle reminders  
**So that** complimenting becomes habitual

**Acceptance Criteria:**
- User sets reminder preferences:
  - Frequency (daily, 3x/week, etc.)
  - Time of day
  - Contexts to focus on
- Smart notifications:
  - "You have a team meeting in 30 min - who could you acknowledge?"
  - "It's Friday! Who made your week better?"
  - "Your streak is at risk - 2 hours until midnight"
- Not spammy - max 1 notification per day
- Easy to snooze or disable

---

## Epic 5: Social & Sharing (Optional)

### User Story 5.1: Anonymous Compliment Exchange
**As a** user wanting to practice with strangers  
**I want to** give and receive compliments anonymously  
**So that** I can build confidence in a safe space

**Acceptance Criteria:**
- "Community Practice" tab
- Users can post asking for compliments on specific things:
  - "I need encouragement about my career change"
  - "I'm proud of my art but unsure if it's good"
- Other users give compliments (anonymously)
- All compliments are reviewed by AI for appropriateness
- No profiles, no follows - just pure practice
- Optional: Can reveal your identity after

---

### User Story 5.2: Share Your Growth
**As a** user proud of my progress  
**I want to** share my achievements  
**So that** I can inspire others

**Acceptance Criteria:**
- Generate shareable images:
  - "I've given 100 genuine compliments!"
  - Aesthetic streak graphics
  - Before/after compliment examples (generic → specific)
- Share to social media or messaging apps
- Includes app link for others to join
- Privacy option: Share stats without actual compliment text

---

## Non-Functional Requirements

### Performance
- App loads in under 2 seconds
- Compliment analysis happens in real-time (no loading spinners)
- Works offline (basic features like practice mode and journal)

### Privacy
- No compliments shared without explicit user consent
- Optional anonymous mode
- Data stored locally by default
- Cloud sync opt-in for multi-device

### Accessibility
- Screen reader compatible
- High contrast mode
- Adjustable text sizes
- Voice input for compliment drafting

### Tone & Design
- Encouraging, never condescending
- Warm color palette (oranges, yellows, soft blues)
- Friendly illustrations
- Conversational copy, not clinical

---

## MVP Scope (Phase 1)

### Must Have:
- Onboarding flow (Stories 1.1, 1.2)
- Context-aware suggestions (Story 2.1)
- Real-time coach (Story 2.2)
- Compliment streak (Story 3.1)
- Basic journal (Story 3.2)

### Can Wait:
- Practice mode (Story 2.3)
- Level/badge system (Story 3.3)
- Compliment library (Story 4.1)
- Social features (Epic 5)

---

## Implementation Notes

### Technical Considerations
- **AI/ML for real-time analysis**: Use sentiment analysis and NLP to evaluate compliment specificity
- **Local-first architecture**: Core features work offline, sync when online
- **Push notifications**: Implement thoughtful reminder system
- **Data privacy**: Encrypt journal entries, give users full control over their data

### Potential Integrations
- Calendar access (for meeting-based reminders)
- Contacts (to suggest people to compliment)
- Social media (for sharing achievements)

### Monetization Strategy
- **Freemium model**:
  - Free: Basic coaching, 5 compliments/day tracked, 7-day streak
  - Premium ($4.99/month): Unlimited tracking, advanced analytics, practice mode, ad-free
- **One-time unlock** ($14.99): Lifetime access to all features

---

## Future Enhancements (Phase 2+)

- Multi-language support
- Voice input and analysis
- Integration with workplace tools (Slack, Teams) for professional context
- Couple's mode (practice complimenting your partner)
- Kids version (teach children to give genuine praise)
- Cultural sensitivity guides (compliments vary across cultures)
- Therapist/coach partnerships for deeper behavioral change

---

**Document Version:** 1.0  
**Last Updated:** October 22, 2025  
**Created for:** Compliment Generator Training Wheels Mobile App

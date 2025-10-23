"""
Training data for Compliment Scorer Model

Each example is labeled with:
- score: 1-5 (quality/specificity rating)
- text: the compliment text

Rating Guide:
1 star: Very generic, no specifics (e.g., "good job", "nice")
2 stars: Generic but complete sentence
3 stars: Some specificity or one specific element
4 stars: Specific with details about what/why/how
5 stars: Highly specific with action + method + impact + meaning
"""

training_data = [
    # 1-star examples (very generic)
    {"text": "Good job", "score": 1},
    {"text": "Nice", "score": 1},
    {"text": "Great work", "score": 1},
    {"text": "Well done", "score": 1},
    {"text": "Thanks", "score": 1},
    {"text": "Cool", "score": 1},
    {"text": "Awesome", "score": 1},
    {"text": "Nice work", "score": 1},
    {"text": "Great", "score": 1},
    {"text": "Good", "score": 1},
    {"text": "That's great", "score": 1},
    {"text": "You're the best", "score": 1},
    {"text": "Amazing", "score": 1},
    {"text": "Fantastic", "score": 1},
    {"text": "You rock", "score": 1},

    # 2-star examples (generic but complete)
    {"text": "You did a great job on that", "score": 2},
    {"text": "That was really good work", "score": 2},
    {"text": "I appreciate your help with this", "score": 2},
    {"text": "You're really talented", "score": 2},
    {"text": "That presentation was great", "score": 2},
    {"text": "Nice job on the project", "score": 2},
    {"text": "You're a great team player", "score": 2},
    {"text": "Thanks for your hard work", "score": 2},
    {"text": "You have a great attitude", "score": 2},
    {"text": "I really like your style", "score": 2},
    {"text": "You're very creative", "score": 2},
    {"text": "That was impressive", "score": 2},
    {"text": "You have good ideas", "score": 2},
    {"text": "You're very professional", "score": 2},
    {"text": "That outfit looks nice on you", "score": 2},
    {"text": "You have a great smile", "score": 2},
    {"text": "You're very helpful", "score": 2},
    {"text": "Thanks for being awesome", "score": 2},
    {"text": "You did well today", "score": 2},
    {"text": "That was a good effort", "score": 2},

    # 3-star examples (some specificity)
    {"text": "Your presentation had really clear slides", "score": 3},
    {"text": "I appreciate how you stayed late to help", "score": 3},
    {"text": "That blue jacket looks great on you", "score": 3},
    {"text": "You explained that concept very clearly", "score": 3},
    {"text": "I noticed you helped the new team member get set up", "score": 3},
    {"text": "Your attention to detail on this report was excellent", "score": 3},
    {"text": "The way you handled that difficult customer was professional", "score": 3},
    {"text": "You have a talent for making people feel comfortable", "score": 3},
    {"text": "I like how you organized the meeting agenda", "score": 3},
    {"text": "Your code is always well-documented", "score": 3},
    {"text": "You're really good at problem-solving", "score": 3},
    {"text": "I appreciate your positive attitude during the project", "score": 3},
    {"text": "That color really suits your skin tone", "score": 3},
    {"text": "You have a gift for writing clear emails", "score": 3},
    {"text": "The research you did for this was thorough", "score": 3},
    {"text": "You're always willing to help when asked", "score": 3},
    {"text": "I noticed you finished that ahead of schedule", "score": 3},
    {"text": "Your ideas in the brainstorm were creative", "score": 3},
    {"text": "You handled that stressful situation calmly", "score": 3},
    {"text": "The way you coordinate tasks is efficient", "score": 3},

    # 4-star examples (specific with details)
    {"text": "The way you broke down that complex problem into clear steps made it so much easier for the team to understand and tackle", "score": 4},
    {"text": "I noticed how you stayed after the meeting to help Sarah understand the new process. That kind of mentorship really strengthens our team", "score": 4},
    {"text": "Your presentation yesterday had excellent data visualization that made the trends immediately obvious. The stakeholders commented on how clear it was", "score": 4},
    {"text": "When you explained the technical concept using that cooking analogy, it finally clicked for me. Your ability to translate complex ideas is remarkable", "score": 4},
    {"text": "The way you handled the client's complaint with empathy while still setting boundaries showed real emotional intelligence and professionalism", "score": 4},
    {"text": "I appreciate how you proactively sent status updates every Friday. It saved me from having to chase down information and helped me plan better", "score": 4},
    {"text": "Your code review comments are always constructive and specific. They help me learn better practices without feeling criticized", "score": 4},
    {"text": "The fact that you remembered my coffee order after meeting once shows incredible attention to detail and thoughtfulness", "score": 4},
    {"text": "How you coordinated three different teams across time zones for that launch was masterful. Your organizational skills prevented what could have been chaos", "score": 4},
    {"text": "That jacket fits you perfectly and the color brings out your eyes. You clearly have a great sense of what works for you", "score": 4},
    {"text": "When you defused that tense moment in the meeting with humor, you helped everyone relax and get back to productive discussion", "score": 4},
    {"text": "Your consistent communication during the project kept everyone aligned and prevented the misunderstandings we had on previous projects", "score": 4},
    {"text": "The research you compiled was exactly what we needed and saved the team probably 20 hours of work. That foresight was invaluable", "score": 4},
    {"text": "The way you mix patterns without it feeling overwhelming takes real confidence and style sense. It works beautifully", "score": 4},
    {"text": "How you asked clarifying questions before jumping into the solution shows maturity and strategic thinking that's rare at your level", "score": 4},
    {"text": "Your willingness to take on the unglamorous documentation work meant the next team can actually understand our decisions. That's leadership", "score": 4},
    {"text": "When you noticed I was struggling and offered specific help without making me ask, it made a difficult week manageable. Thank you", "score": 4},
    {"text": "The examples you used in your training session were perfectly chosen for our audience's experience level. People really engaged because of that", "score": 4},
    {"text": "Your calm presence during the system outage helped the team stay focused on solutions instead of panicking. That steadiness matters", "score": 4},
    {"text": "How you give feedback - starting with what worked before suggesting improvements - makes people actually want to hear your thoughts", "score": 4},

    # 5-star examples (highly specific with full structure)
    {"text": "I noticed how you restructured the onboarding process by adding weekly check-ins and a buddy system. The way you anticipated new hires' questions before they asked showed deep empathy. The result is that our retention in the first 90 days improved by 30%, and every new hire mentions feeling supported. That thoughtful redesign has fundamentally changed our team culture for the better", "score": 5},
    {"text": "When you presented the Q3 results, you didn't just show numbers - you told a story with data, using color-coded trends and highlighting the 'why' behind each metric. Your preparation showed when you had backup slides for every possible question. The CEO specifically mentioned your presentation as a model for the company because it made complex financial data accessible and actionable for non-finance stakeholders. That skill in communication creates real business impact", "score": 5},
    {"text": "The way you handled the client crisis last Thursday demonstrated exceptional judgment. When they called angry about the delay, you listened fully before responding, acknowledged their frustration specifically, and then presented three options with clear tradeoffs. You didn't just solve the immediate problem - you rebuilt trust by being transparent about what went wrong and how we'd prevent it. The client told me they actually feel more confident in us now than before the issue. That's transformative relationship management", "score": 5},
    {"text": "I've been watching how you mentor junior developers, and what stands out is your method. You don't give answers - you ask questions that guide them to solutions, then explain the reasoning behind best practices. When Jake told me he finally understands testing because of your patient explanations using real examples from our codebase, it highlighted your gift for teaching. You're not just making our code better, you're making our developers better. That investment in people is what great technical leadership looks like", "score": 5},
    {"text": "Your decision to restructure the database schema, even though it meant extra work short-term, has paid off enormously. The queries that used to take 30 seconds now run in under 2 seconds, which means our users aren't abandoning their searches anymore. What impressed me most was how you documented the migration process so thoroughly that other teams have used it as a template. You took on unglamorous infrastructure work that users will never see, but which fundamentally improved their experience. That's the kind of engineering excellence that compounds over time", "score": 5},
    {"text": "When you noticed that Sarah was being talked over in meetings, you didn't just feel bad about it - you actively redirected attention to her ideas and created space for her to finish her thoughts. Over the past month, I've watched her confidence grow and her contributions increase because you consistently amplified her voice. You didn't make a big deal about it or expect recognition; you just saw something wrong and fixed it with intention and consistency. That quiet advocacy for others is rare and creates psychological safety that makes teams thrive", "score": 5},
    {"text": "The innovation sprint you organized wasn't just another brainstorming session. You structured it with research on effective ideation, invited diverse perspectives from across departments, created an environment where wild ideas felt safe, and then had a clear process for evaluation. Three of the concepts from that session are now in production, including the feature that customers have rated as their favorite addition this year. You took what could have been a fluffy exercise and turned it into measurable business value. That ability to execute on creativity is what drives companies forward", "score": 5},
    {"text": "I want to acknowledge how you've approached the challenge of coordinating the remote team across eight time zones. You implemented async standups that respect everyone's schedule, created documentation practices that reduce the need for meetings, and established core overlap hours that balance everyone's needs. Since these changes, our velocity has increased 40% and team satisfaction scores are the highest they've been. What makes this remarkable is that you solicited input from the team, tested different approaches, and iterated based on feedback rather than imposing a solution. You solved a complex organizational problem with both data and empathy", "score": 5},
    {"text": "The way you've grown over this past year has been remarkable to witness. When you started, you were technically strong but struggled with ambiguity. Now you're seeking out the messy, undefined problems because you've developed the confidence to structure them yourself. The initiative you took on the API redesign - identifying the problem, proposing the solution, building consensus, and executing - would have been inconceivable a year ago. What I admire most is your self-awareness: you actively sought feedback, worked on specific skills, and applied what you learned. That commitment to growth is what separates good engineers from great ones", "score": 5},
    {"text": "Your outfit today is perfection - that emerald blazer with the tailored black pants creates such a polished silhouette, and the gold accessories add just enough warmth without overwhelming. What I really admire is how you've developed a signature style that's both professional and uniquely you. The confidence you wear your clothes with is as striking as the clothes themselves. You've clearly invested time understanding what colors, cuts, and styles work for your body and personality, and it shows. The way you present yourself opens doors because people perceive competence, creativity, and attention to detail before you even speak. That's the power of intentional style", "score": 5},
]

def get_training_data():
    """Returns the training dataset as a list of dictionaries"""
    return training_data

def get_data_stats():
    """Returns statistics about the training data"""
    scores = [item['score'] for item in training_data]
    from collections import Counter
    score_counts = Counter(scores)

    return {
        'total_examples': len(training_data),
        'score_distribution': dict(score_counts),
        'avg_score': sum(scores) / len(scores),
    }

if __name__ == '__main__':
    # Print dataset statistics
    stats = get_data_stats()
    print("Training Data Statistics:")
    print(f"Total examples: {stats['total_examples']}")
    print(f"Score distribution: {stats['score_distribution']}")
    print(f"Average score: {stats['avg_score']:.2f}")

    # Show example from each score level
    print("\nExample from each score level:")
    for score in range(1, 6):
        example = next(item for item in training_data if item['score'] == score)
        print(f"\n{score} stars: \"{example['text']}\"")

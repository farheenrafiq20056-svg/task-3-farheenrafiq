# Project 3: AI Recommendation Logic 🤖
# Tech Stack Recommender - DecodeLabs Batch 2026

# Step 1: Import Libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Step 2: Dataset - Job Roles with Required Skills
job_roles = {
    "Data Scientist": "python machine-learning sql data-analysis statistics numpy pandas deep-learning",
    "Web Developer": "html css javascript react nodejs frontend backend web-design",
    "DevOps Engineer": "aws docker kubernetes linux git ci-cd cloud automation",
    "AI Engineer": "python deep-learning tensorflow pytorch neural-networks machine-learning nlp",
    "Backend Developer": "python java sql apis rest-api databases nodejs backend",
    "Frontend Developer": "html css javascript react vue typescript ui-ux frontend",
    "Cloud Architect": "aws azure cloud docker kubernetes infrastructure devops",
    "Data Analyst": "sql excel python data-analysis visualization power-bi statistics",
    "Cybersecurity Analyst": "networking security linux ethical-hacking firewalls cryptography",
    "Mobile Developer": "flutter dart react-native android ios mobile-apps java kotlin"
}

# Step 3: Prepare Data
role_names = list(job_roles.keys())
role_descriptions = list(job_roles.values())

print("=" * 55)
print("   🤖 AI Tech Stack Recommender")
print("   Powered by TF-IDF + Cosine Similarity")
print("=" * 55)

# Step 4: Take User Input (minimum 3 skills)
print("\n📌 Enter your skills (minimum 3)")
print("Example: python, machine-learning, sql\n")

user_input = input("Your skills: ")
user_skills = [skill.strip().lower() for skill in user_input.split(",")]

if len(user_skills) < 3:
    print("\n⚠️  Please enter at least 3 skills!")
else:
    # Step 5: Convert to TF-IDF Vectors
    user_profile = " ".join(user_skills)
    
    # Add user profile to dataset for vectorization
    all_text = role_descriptions + [user_profile]
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_text)
    
    # Step 6: Calculate Cosine Similarity
    user_vector = tfidf_matrix[-1]  # Last item is user profile
    role_vectors = tfidf_matrix[:-1]  # All job roles
    
    similarities = cosine_similarity(user_vector, role_vectors)[0]
    
    # Step 7: Sort & Filter - Get Top 3
    top_indices = np.argsort(similarities)[::-1][:3]
    
    # Step 8: Display Recommendations
    print("\n" + "=" * 55)
    print("🎯 TOP 3 RECOMMENDED CAREER PATHS FOR YOU:")
    print("=" * 55)
    
    for rank, idx in enumerate(top_indices, 1):
        score = similarities[idx] * 100
        role = role_names[idx]
        
        if score > 0:
            print(f"\n{'🥇' if rank==1 else '🥈' if rank==2 else '🥉'} Rank {rank}: {role}")
            print(f"   📊 Match Score: {score:.1f}%")
            print(f"   🔧 Required Skills: {job_roles[role]}")
        else:
            print(f"\n❌ Rank {rank}: No strong match found")
    
    print("\n" + "=" * 55)
    print("💡 Tip: Add more specific skills for better matches!")
    print("=" * 55)
    
    # Step 9: Show user their profile summary
    print(f"\n📋 Your Skill Profile:")
    print(f"   Skills entered: {len(user_skills)}")
    print(f"   Skills: {', '.join(user_skills)}")
    print("\n✅ Project 3 Complete!")
import pandas as pd

# Sample data for student preferences
data = {
    'preferred_style': ['Visual', 'Auditory', 'Kinesthetic', 'Visual', 'Auditory'],
    'preferred_topic': ['Math', 'Science', 'History', 'Math', 'Science'],
    'learning_path': ['Math - Visual Learners', 'Science - Auditory Learners', 'History - Kinesthetic Learners',
                      'Math - Visual Learners', 'Science - Auditory Learners']
}

# Create DataFrame
df = pd.DataFrame(data) 

# Save DataFrame to CSV
df.to_csv('student_preferences.csv', index=False)

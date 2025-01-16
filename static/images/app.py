from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'name': 'Rahul Boddeda',
        'title': 'Frontend Developer',
        'description': 'good at in Machine Learning and Web-development, producing quality work.',
        'about': 'Web developer with extensive knowledge and years of experience, working in web technologies and UI/UX design, delivering quality work.',
        'years_exp': 'Fresher',
        'completed_projects': '2(Campus level) + 1(Internship)',
        'education': [
            {
                'degree': 'B.Tech in Computer Science',
                'institution': 'National Institute of Technology Andhra Pradesh',
                'year': '2022-2026',
                'CGPA': '8.42'
            },
            {
                'degree': 'BIEAP - Intermediate',
                'institution': 'SASI NEW GEN JR COLLEGE',
                'year': '2020-2022',
                'Marks': '957/1000'
            },
            {
                'degree': 'CISCE - High School',
                'institution': 'De Paul School',
                'year': '2008-2020',
                'Percentage': '94.3%'
            }
        ],
        'skills': {
            'frontend': {
                'HTML': 90,
                'CSS': 85,
                'JavaScript': 80,
                'React': 50
            },
            'backend': {
                'Python': 85,
                'Node.js': 75,
                'SQL': 80
            }
        },
        'services': [
            {
                'title': 'Web Development',
                'description': 'High-quality development of sites at the professional level.',
                'icon': 'fa-code'
            },
            {
                'title': 'Machine Learning',
                'description': 'Integrating ML applications in daily life',
                'icon': 'fa-brain'
            }
        ],
        'experience': [
            {
                'title': 'Pradical Solutions Pvt. Ltd. - Machine Learning Intern',
                'description': 'Utilized the YOLOv8 model to accurately detect missing teeth and perform instance segmentation of the mandibular canal across a dataset of over 2000 images. Created a seamless interactive platform for user engagement and project management. Documented an overview of the entire project in a concise format',
                'image': 'portfolio.jpeg',
                'link': '#'
            }
        ],
        'social_links': {
            'github': 'https://github.com/rahboddeda',
            'linkedin': 'https://linkedin.com/in/rahulboddeda'
        },
        'contact': {
            'email': 'rahulboddeda@gmail.com',
            'phone': '+91 6303793820',
            'location': 'Visakhapatnam, India'
        }
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True) 
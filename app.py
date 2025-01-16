from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'name': 'Rahul Boddeda',
        'title': 'Frontend Developer',
        'description': 'good at in Machine Learning and Web-development, producing quality work.',
        'about': """Motivated Computer Science student with hands-on experience in developing AI-driven solutions, web
 applications, and software platforms. Eager to leverage technical skills in machine learning, data science, and
 full-stack development to contribute to innovative projects as an intern. Seeking opportunities to collaborate
 on real-world challenges, enhance my expertise in emerging technologies, and deliver impactful results""",
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
                'SQL': 80,
                'Flask':90,
            }
        },
        'experience': [
            {
                'title': 'Pradical Solutions Pvt. Ltd. - Machine Learning Intern',
                'duration': 'May 2024 - July 2024',
                'description': 'Utilized the YOLOv8 model to accurately detect missing teeth and perform instance segmentation of the mandibular canal across a dataset of over 2000 images. Created a seamless interactive platform for user engagement and project management. Documented an overview of the entire project in a concise format',
                'image': 'portfolio.jpeg',
                'link': '#'
            }
        ],
        'projects': [
            {
                'title': 'Smart Automatic Attendance System',
                'description': [
                    'Developed Smart Attendance System for Large Organisations. Implemented facial recognition for facial detection and recognition.',
                    'Created an SQL database, ensuring correct and safe data storage.',
                    'Used face recognition module, SQL, Node JS Technologies.'
                ],
                'icon': 'fa-id-badge'
            },
            {
                'title': 'Mock IRCTC E-Ticketing Modules',
                'description': [
                    'A Node JS-based web application that allows users to reserve preferred seats in real time.',
                    'Interactive Booking Interface: Easily select stations, view distance-calculated ticket prices, and choose seats from a visual coach layout.',
                    'Technology Used: HTML, CSS, and Flask'
                ],
                'icon': 'fa-train'
            }
        ],
        'social_links': {
            'github': 'https://github.com/rahboddeda',
            'linkedin': 'https://www.linkedin.com/in/rahul-boddeda-903742262/'
        },
        'contact': {
            'email': 'rahulboddeda@gmail.com',
            'phone': '+91 6303793820',
            'location': 'Visakhapatnam, India'
        },
        'certifications': [
            {
                'title': 'Accenture UK developer and technology virtual experience programme',
                'issuer': 'Forage',
                'date': 'Dec 2024',
                'points': [
                    'Completed the Developer and Technology Job Simulation where I developed an end to end understanding of the Software Development Life cycle',
                    'Conducted in-depth research into emerging technology trends, particularly in the field of DevOps, demonstrating a proactive approach to staying informed about the rapidly evolving tech landscape',
                    'Created and delivered a compelling PowerPoint presentation analyzing and comparing Waterfall and Agile methodologies.'
                ],
                'icon': 'fa-certificate'
            },
            {
                'title': 'AI for Beginners',
                'issuer': 'HP LIFE',
                'date': 'Dec 2024',
                'points': [
                    'I learnt about Core AI Concepts',
                    'The fundamentals of AI and how it operates',
                    'Importance of Data',
                    'Why data is essential for training AI and driving its effectiveness',
                    'Real-World Applications',
                    'Insights into how AI is revolutionizing businesses and industries.',
                    'Ethical Implications',
                    'The importance of addressing challenges like bias, transparency, and accountability in AI.'
                ],
                'icon': 'fa-robot'
            }
        ],
        'responsibilities': [
            {
                'title': 'Secretary of Design team Graphic Cafe- NIT ANP, Tadepalligudem',
                'duration': 'Oct 2024- Oct 2025',
                'points': [
                    'Collaborate with cross-functional teams to create designs that effectively communicate messages and resonate with target audiences. Drive the adoption of new design trends and technologies to enhance efficiency and creativity.',
                    'Spearhead the creative vision and execution of design projects, ensuring alignment with brand identity and strategic goals. Lead and mentor a team of designers, encouraging collaboration and innovation to deliver high impact visual solutions'
                ],
                'icon': 'fa-users'
            }
        ]
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True) 
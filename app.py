from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Sample product data
PRODUCT = {
    'name': 'ProTech X1',
    'tagline': 'Revolutionize Your Workflow',
    'description': 'The ultimate productivity tool that combines AI-powered automation with intuitive design. Boost your team\'s efficiency by 300% with our cutting-edge technology.',
    'price': '$49.99',
    'features': [
        '⚡ AI-Powered Automation',
        '📊 Real-time Analytics',
        '🔒 Enterprise-Grade Security',
        '🌐 Cloud Sync Across Devices',
        '📱 Mobile & Desktop Apps',
        '🔄 24/7 Customer Support'
    ],
    'image': 'https://via.placeholder.com/600x400/4A90E2/FFFFFF?text=ProTech+X1'
}

# Testimonials data
TESTIMONIALS = [
    {
        'name': 'Sarah Johnson',
        'role': 'CEO, TechStart Inc.',
        'content': 'This product transformed how we work. Our productivity increased by 200% in just two weeks!',
        'rating': 5
    },
    {
        'name': 'Michael Chen',
        'role': 'CTO, CloudSys Solutions',
        'content': 'The AI features are incredible. It\'s like having an extra team member who never sleeps.',
        'rating': 5
    },
    {
        'name': 'Emily Rodriguez',
        'role': 'Product Manager, InnovateLab',
        'content': 'Best investment we made this year. The interface is intuitive and the support is outstanding.',
        'rating': 5
    }
]

@app.route('/')
def index():
    """Render the main landing page"""
    return render_template('index.html', 
                         product=PRODUCT, 
                         testimonials=TESTIMONIALS,
                         year=datetime.now().year)

@app.route('/api/subscribe', methods=['POST'])
def subscribe():
    """Handle newsletter subscription"""
    email = request.json.get('email')
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    # In production, save to database
    # For demo, just return success
    return jsonify({
        'message': f'Successfully subscribed with {email}!',
        'status': 'success'
    })

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submission"""
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    
    if not all([name, email, message]):
        return jsonify({'error': 'All fields are required'}), 400
    
    # In production, send email or save to database
    print(f"Contact Form Submission:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")
    
    return jsonify({
        'message': 'Thank you for your message! We\'ll get back to you soon.',
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

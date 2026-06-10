from flask import Flask
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return f'''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AWS ECR/ECS Demo</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .container {{
                background: white;
                border-radius: 20px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                padding: 40px;
                max-width: 600px;
                width: 90%;
                text-align: center;
            }}
            .logo {{
                font-size: 3em;
                margin-bottom: 20px;
            }}
            h1 {{
                color: #232F3E;
                margin-bottom: 30px;
                font-size: 2.2em;
            }}
            .status-card {{
                background: #f8f9fa;
                border-left: 5px solid #28a745;
                padding: 20px;
                margin: 20px 0;
                border-radius: 10px;
                text-align: left;
            }}
            .info-grid {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
                margin: 30px 0;
            }}
            .info-item {{
                background: #e9ecef;
                padding: 15px;
                border-radius: 10px;
            }}
            .info-label {{
                font-weight: bold;
                color: #495057;
                font-size: 0.9em;
                margin-bottom: 5px;
            }}
            .info-value {{
                color: #232F3E;
                font-size: 1.1em;
            }}
            .tech-stack {{
                display: flex;
                justify-content: center;
                gap: 15px;
                margin: 30px 0;
                flex-wrap: wrap;
            }}
            .tech-badge {{
                background: #FF9900;
                color: white;
                padding: 8px 16px;
                border-radius: 20px;
                font-size: 0.9em;
                font-weight: bold;
            }}
            .footer {{
                margin-top: 30px;
                color: #6c757d;
                font-size: 0.9em;
            }}
            @media (max-width: 600px) {{
                .info-grid {{ grid-template-columns: 1fr; }}
                .tech-stack {{ flex-direction: column; align-items: center; }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo"></div>
            <h1>AWS ECR/ECS Demo</h1>
            
            <div class="status-card">
                <strong>✅ Aplicação rodando com sucesso!</strong>
                <p>Teste rodando no Elastic Beanstalk</p>
            </div>
            
            <div class="footer">
                <p><strong>Demonstração:</strong> Pipeline completo de containerização e deploy na AWS</p>
                <p>Código → Docker → ECR → ECS → Produção</p>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {{
        'status': 'healthy',
        'service': 'aws-ecs-demo',
        'hostname': socket.gethostname(),
        'timestamp': datetime.now().isoformat()
    }}

@app.route('/info')
def info():
    return {{
        'application': 'AWS ECR/ECS Demo',
        'version': '1.0.0',
        'hostname': socket.gethostname(),
        'environment': os.environ.get('ENVIRONMENT', 'production'),
        'port': 80,
        'framework': 'Flask',
        'container': 'Docker',
        'registry': 'AWS ECR',
        'orchestrator': 'AWS ECS'
    }}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

"""Inicialização local com preparação do banco antes de aceitar requisições."""
import os
from . import create_app, SOURCE


def main():
    port = int(os.environ.get('PORT', '8080'))
    if port in {5000, 6000}:
        raise SystemExit('Use PORT=8080: a porta 5000 conflita com AirPlay e a 6000 é bloqueada por navegadores.')
    app = create_app()
    app.extensions['database'].prepare(SOURCE)
    print(f"Banco SQLite: {app.extensions['db_engine'].url.database}", flush=True)
    print(f'Abra no navegador: http://127.0.0.1:{port}/', flush=True)
    app.run(host='127.0.0.1', port=port, load_dotenv=False)


if __name__ == '__main__':
    main()

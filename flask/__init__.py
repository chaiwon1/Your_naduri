from flask import Flask


def create_app(config=None):
    """
    create_app 은 애플리케이션 팩토리 패턴에 따른 함수입니다.

    config 파라미터는 테스트에 필요하니 변경하지는 말아주세요!
    """
    app = Flask(__name__)
    
    # 여기에서 주어진 config 에 따라 추가 설정을 합니다.
    if config is not None:
        app.config.update(config)

    from views.error import error_bp 
    from views.home import home_bp
    from views.predict import predict_bp
    from views.recommand import recommand_bp

    app.register_blueprint(error_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(predict_bp)
    app.register_blueprint(recommand_bp)

    return app

if __name__ == "__main__":
  app = create_app()
  app.run()
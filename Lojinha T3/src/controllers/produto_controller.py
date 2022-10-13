
from src.models.produto import Produto

class ProdutoController:
    def __init__(self):
        self._produto = [
            Produto("Miojo sabor galinha", 10.00, "https://liasupermercado.com.br/wp-content/uploads/2022/02/7891079000212.jpg"),
            Produto("Monster Mango", 15.00, "https://muffatosupermercados.vteximg.com.br/arquivos/ids/303108-400-400/0070847033301.jpg?v=637758755771800000"),
            Produto("Café do Starbucks", 20.00, "https://static.vecteezy.com/ti/vetor-gratis/t1/226343-cafe-starbucks-gr%C3%A1tis-vetor.jpg"),
            Produto("Temaki de Salmão", 35.00, "https://pos.motorburguer.com.br/wp-content/uploads/2021/01/temaki-filadelfia.jpg"),
            Produto("IPhone 14 Pro Max", 15000.00, "https://s2.glbimg.com/0kn766R4SXAcROc-lXyU2fXAMLM=/400x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2022/H/M/lkvG33T2miHGAkznrY1w/14-pro-preto-espacial-ok.jpg"),
            Produto("Samsung S22 Ultra", 8000.00, "https://t.ctcdn.com.br/jU3NkVQ7myO2NkDgahBggUQz8-c=/fit-in/400x400/filters:format(webp):fill(transparent):watermark(wm/prd.png,-32p,center,1,none,15)/i559673.png"),
            Produto("RTX4090", 15000.00, "https://cdn.vox-cdn.com/thumbor/QKrWcDCOAusI_TZpGVC7GwQG0Tg=/400x0/filters:no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/24044001/SG_BOX01_card_rgb.png"),
            Produto("Logitech G Pro X Superlight",700.00, "https://images.kabum.com.br/produtos/fotos/149990/mouse-sem-fio-gamer-logitech-g-pro-x-superlight-lightspeed-5-botoes-25000-dpi-branco-910-005941_1614261697_g.jpg")
        ]

    def get_produto(self,index):
        return self._produto[index]
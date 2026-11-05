import asyncio, html
from playwright.async_api import async_playwright

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1350px;font-family:'Inter',sans-serif;color:#fff;position:relative;overflow:hidden;
background:radial-gradient(900px 700px at 100% 0%,#2456F5 0%,rgba(36,86,245,0) 60%),linear-gradient(160deg,#0B1F3A 0%,#0A1730 100%)}
.top{position:absolute;left:84px;top:80px;right:84px;display:flex;justify-content:space-between;align-items:center}
.brand{display:flex;align-items:center;gap:14px;font-weight:700;font-size:34px;letter-spacing:-.5px}
.dot{width:22px;height:22px;border-radius:50%;background:#25D366;box-shadow:0 0 0 8px rgba(37,211,102,.18)}
.tag{font-size:24px;font-weight:600;color:#9DB4E8;letter-spacing:.5px;text-transform:uppercase}
.main{position:absolute;left:84px;right:84px;top:250px;bottom:190px;display:flex;flex-direction:column;justify-content:center}
h1{font-family:'Inter Display','Inter',sans-serif;font-weight:800;font-size:104px;line-height:1.04;letter-spacing:-3px}
h1 em{font-style:normal;color:#25D366}
h1.sm{font-size:88px}
p.sub{margin-top:44px;font-size:42px;line-height:1.35;color:#C9D6F2;font-weight:500;max-width:880px}
.foot{position:absolute;left:84px;right:84px;bottom:80px;display:flex;justify-content:space-between;align-items:center;font-size:28px;color:#9DB4E8;font-weight:600}
.pill{background:#25D366;color:#06210F;font-weight:800;font-size:30px;padding:20px 36px;border-radius:999px}
.pill.blue{background:#2456F5;color:#fff}
.chat{margin-top:56px;display:flex;flex-direction:column;gap:22px}
.b{max-width:800px;padding:26px 34px;border-radius:30px;font-size:38px;line-height:1.35;font-weight:500}
.me{align-self:flex-end;background:#25D366;color:#06210F;border-bottom-right-radius:8px}
.her{align-self:flex-start;background:#fff;color:#0B1F3A;border-bottom-left-radius:8px}
.her b{font-weight:800}
.note{margin-top:30px;font-size:26px;color:#8FA6D6}
.steps{margin-top:50px;display:flex;flex-direction:column;gap:22px}
.st{display:flex;align-items:center;gap:28px;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.14);border-radius:28px;padding:30px 36px;font-size:44px;font-weight:700}
.st span{width:64px;height:64px;border-radius:50%;background:#2456F5;display:flex;align-items:center;justify-content:center;font-size:34px;flex:none}
"""
def page(tag, body, foot):
    return f"""<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="top"><div class="brand"><div class="dot"></div>sua gerente IA</div><div class="tag">{tag}</div></div>
<div class="main">{body}</div>
<div class="foot">{foot}</div></body></html>"""

HAND="<span>@suagerente360</span>"
cards = {
"01-apresentacao": page("Conheça",
 "<h1>Sua loja ganhou uma <em>gerente.</em> Ela é de IA.</h1><p class='sub'>Metas, vendas e equipe pelo WhatsApp, ligada ao ERP da sua loja ou franquia.</p>",
 HAND+"<div class='pill'>Teste grátis · link na bio</div>"),
"02-pergunta-meta": page("Rotina de loja",
 "<h1>Seu vendedor pergunta a <em>meta do mês</em> toda semana?</h1><p class='sub'>Quando a meta mora numa planilha, ninguém sabe onde a loja está de verdade.</p>",
 HAND+"<span>Deslize ou salve ➜</span>"),
"03-meta-diaria": page("Rotina de loja",
 "<h1>Quanto eu preciso vender <em>hoje</em>?</h1><p class='sub'>Se o vendedor não sabe a meta do dia, ele vende no escuro e a meta do mês escapa.</p>",
 HAND+"<span>Já passou por isso?</span>"),
"04-planilha": page("Controle de metas",
 "<h1>A planilha de metas que <em>ninguém abre.</em></h1><p class='sub'>Atualizada tarde, copiada errada e perdida no meio das conversas do WhatsApp.</p>",
 HAND+"<span>Tem uma dessas aí?</span>"),
"05-fim-6x1": page("Escala de trabalho",
 "<h1 class='sm'>Fim da 6x1: sua <em>escala</em> fecha?</h1><p class='sub'>A partir de 15/12/2026 a jornada cai para 42h por semana, com duas folgas semanais. Simule como fica a sua loja.</p>",
 HAND+"<div class='pill blue'>Simulador grátis · link na bio</div>"),
"06-hora-extra": page("Escala de trabalho",
 "<h1 class='sm'>Hora extra: o <em>custo escondido</em> da nova escala.</h1><p class='sub'>Compare modelos de escala 5x2 e veja quantas horas extras cada um gera na sua loja.</p>",
 HAND+"<div class='pill blue'>Simule grátis · link na bio</div>"),
"07-whatsapp": page("Como funciona",
 "<h1 class='sm'>Pergunte no WhatsApp. Ela <em>responde.</em></h1><div class='chat'><div class='b me'>Como estamos na meta do mês?</div><div class='b her'>Faltam <b>R$ 12.400</b> para a meta. Para fechar, a loja precisa vender <b>R$ 1.800 por dia</b>.</div></div><div class='note'>Exemplo ilustrativo, com valores fictícios.</div>",
 HAND+"<span>Sua Gerente IA</span>"),
"08-meta-vendedor": page("Para a equipe",
 "<h1 class='sm'>Cada vendedor sabe sua <em>meta do dia.</em></h1><div class='steps'><div class='st'><span>1</span>Meta do mês</div><div class='st'><span>2</span>Meta por dia</div><div class='st'><span>3</span>Quanto falta hoje</div></div>",
 HAND+"<span>Sem calculadora</span>"),
"09-teste-gratis": page("Teste grátis",
 "<h1>Teste a <em>Sua Gerente IA</em> na sua loja.</h1><p class='sub'>Conecte ao seu ERP e acompanhe vendas e metas conversando pelo WhatsApp.</p>",
 HAND+"<div class='pill'>Link na bio</div>"),
}
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':1080,'height':1350}, device_scale_factor=1)
        for name, h in cards.items():
            await pg.set_content(h)
            await pg.wait_for_timeout(150)
            await pg.screenshot(path=f"{name}.png")
        await b.close()
asyncio.run(main())

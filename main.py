import discord
import random
import openai
from discord.ext import commands

intents = discord.Intents.all()
intents.voice_states = True
intents.messages = True
intents.members = True
intents.typing = True
intents.presences = True

openai.api_key = ""

bot = commands.Bot(command_prefix='/poof ', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot está pronto como {bot.user}')

@bot.command()
async def tafunfando(ctx):
    print("Respondeu (tafunfando)")

    respostas = [
        "Sim, mano...", "To aqui...", "Não", "Certamente, bobão!", "Não sei, não gosto de fofoca."
    ]
    resposta = random.choice(respostas)
    await ctx.send(f"{resposta}")
    return

@bot.command()
async def calaaboca(ctx):
    print("Respondeu (calaaboca)")

    respostas = [
        "Como vou calar a boca se estou digitando e enviando mensagens no chat?", "Cala a boca já morreu, quem manda na minha boca sou eu!", "Vem calar!"
    ]
    resposta = random.choice(respostas)
    await ctx.send(f"{resposta}")
    return

@bot.command()
async def sorteia(ctx):
    print("Respondeu (sorteia)")

    guild = ctx.guild

    for voice_channel in guild.voice_channels:
        if voice_channel:
            voice_states = voice_channel.voice_states

            if voice_states:
                random_member_id = random.choice(list(voice_states.keys()))
                member = guild.get_member(random_member_id)

                if member:
                    respostas = [
                        "adora um bandeclay", "tomou um mebous", "colocou togles no bandeclay"
                    ]
                    resposta = random.choice(respostas)
                    await ctx.send(f"{member.mention}, {resposta}")
                    return

    await ctx.send("Não foi possível encontrar um bobão para sortear.")

@bot.command()
async def dedura(ctx, member: discord.Member):
    print("Respondeu (dedura)")

    respostas = [
        "adora um bandeclay", "tomou um mebous", "colocou togles no bandeclay"
    ]
    resposta = random.choice(respostas)
    await ctx.send(f"{member.mention}, {resposta}")
    return

@bot.command()
async def explana(ctx, member: discord.Member, memberdois: discord.Member):
    print("Respondeu (explana)")

    respostas = [
        "roubou o bandeclay do", "escondeu o togles do", "colocou sal no mebous do"
    ]
    resposta = random.choice(respostas)
    await ctx.send(f"{member.mention}, {resposta} {memberdois.mention}")
    return

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        temperature=0.8,
    )
    return response.choices[0].text.strip()

@bot.command()
async def responde(ctx, *, question):
    prompt = f"Ah, claro, vamos resolver o mistério, seu espertão. Você pergunta: '{question}'."
    response = generate_response(prompt)
    await ctx.send(response)

bot.run('')
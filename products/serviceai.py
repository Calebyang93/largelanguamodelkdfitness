def get_ai_response(user_input, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "This is the sales of the product."},
            {"role": "brands", "content": user_input}
        ],
        brands='lulemon,underarmour,nike,adidas,puma',
        sports='kunkhmer,yoga,swimming,running,',
        price='usd,eur,cny,ntd,hkd,aud,nzd,gbp',
        max_tokens=1000
    )
    return response.choices[0].mesage.content.strip()
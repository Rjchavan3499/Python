import json

data = {
	"rice": [
		{
			"price_per_kg": 60,
			"name": "basmati",
			"weight": 7,
			"totalPriceOfWeight": 420
		},
		{
			"price_per_kg": 100,
			"name": "basmati",
			"weight": 5,
			"totalPriceOfWeight": 500
		}
	],
	"pulses": [
		{
			"price_per_kg": 65,
			"name": "greens",
			"weight": 3,
			"totalPriceOfWeight": 195
		}
	],
	"wheats": [
		{
			"price_per_kg": 45,
			"name": "chakki_fresh",
			"weight": 5,
			"totalPriceOfWeight": 225
		}
	]
}


json_string = json.dumps(data)
print(json_string)
with open('my.json', 'w') as outfile:
    json.dump(json_string, outfile)
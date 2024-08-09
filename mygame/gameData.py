rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'item' : ['muscle man'],
                  'description' : "On the walls, you see glamour shots of an unknown family covered in dust.  This house obviously hasn't been occupied by the living in quite some time.  You see the kitchen to the south and the dining room to the east."
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'south' : 'Living Room',
                  'item' : ['ghoul', 'twinkie'],
                  'description': 'The kitchen looks eerily like your kitchen from childhood, right down to the brown geometric patterned linoleum floor.  You see the hall to the north, and the living room to the south.'
                },
            'Dining Room' :{
                  'west': 'Hall',
                  'south': 'Garden',
                  'item': ['potion'],
                  'description': 'The dining room looks kind of cool actually, like it belongs in the  apartment from three men and a baby! You see the Hall to the west and the garden to the south.'
                },
            'Garden' : {
                    'north' : 'Dining Room',
                    'south' : 'Garden Gate',
                    'description': 'You see a sprawling garden overgrown with weeds.  You see the dining room to the north, and what\'s that in the distance to the south...it looks like a gate...'
                },
            'Garden Gate' :{
                    'north': 'Garden',
                    'description': 'Rats!!! The gate is locked!',
                    'description2': 'You look closer and see a message scratched into the gate'
                },
            'Living Room' : {
                'north' : 'Kitchen',
                'west' : 'Bathroom',
                'east' : 'Bedroom',
                'description': 'You see a bathroom to the east and a bedroom to the west.'
                },
            'Bathroom' : {
                'east' : 'Living Room',
                'item' : ['note', 'comb'],
                'message': 'There is only one word written on the note....the word "glove"',
                'description': 'Wow, a bidet!  You see the living room back to the east.'

                },
            'Bedroom' :{
                'west' : 'Living Room',
                'item' : ['mystery box 1', 'mystery box 2'],
                'description': 'Water bed!!!! You see the living room to the west'
                }
         }

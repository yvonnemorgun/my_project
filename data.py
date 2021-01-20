from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbsparta

questions = []
questions.append({"idx":1, "text":"눈을 떠보니 꽃집입니다. 어떤 꽃을 고르시겠어요?"})
questions.append({"idx":2, "text":"눈을 떠보니 카오산로드의 과일 가게입니다. 어떤 과일을 구매 하시겠습니까?"})
questions.append({"idx":3, "text":"눈을 떠보니 허브정원에서 화분을 증정하고 있습니다. 어떤 식물을 가져가시겠습니까?"})
questions.append({"idx":4, "text":"눈을 떠보니 깊숙한 산속입니다.어떤 나무와 동물의 향기가 인상깊으신가요? "})
questions.append({"idx":5, "text":"자, 이제 마지막 여행지 입니다. 눈을 떠보니 바다가 보이는 까페입니다. 마음에 드는 향을 골라보세요."})
db.questions.insert_many(list(questions))

answers = []
answers.append({"question_idx":1, "answer_idx":1, "text":"장미", "desc":"여성스럽고 진한 매혹적인 꽃향을 좋아하며,"})
answers.append({"question_idx":1, "answer_idx":2, "text":"자스민", "desc":"은은하면서도 매력적인 여성미가 풍부한 향을 좋아하며,"})
answers.append({"question_idx":1, "answer_idx":3, "text":"아카시아", "desc":"청순하고 달달하고 깨끗한 꽃향을 좋아하며,"})
answers.append({"question_idx":1, "answer_idx":4, "text":"라일락", "desc":"달큰하고 풍부한 꽃향을 좋아하며,"})
answers.append({"question_idx":1, "answer_idx":5, "text":"은방울", "desc":"청순하면서 은은한 실크같은 꽃향을 좋아하며,"})
answers.append({"question_idx":1, "answer_idx":6, "text":"국화", "desc":"신선한 풀향이 나는 꽃향을 좋아하며,"})
answers.append({"question_idx":1, "answer_idx":7, "text":"튤립", "desc":"깨끗하고 가벼운 꽃향을 좋아하며,"})
answers.append({"question_idx":1, "answer_idx":8, "text":"꽃향을 좋아하지 않습니다.", "desc":"꽃향은 좋아하지 않습니다."})

answers.append({"question_idx":2, "answer_idx":9, "text":"레몬", "desc":"가볍게 상큼하고 새콤 과일향을 좋아하며,"})
answers.append({"question_idx":2, "answer_idx":10, "text":"자몽", "desc":"약간 씁쓸하면서 한새콤한 과일향을 좋아하며,"})
answers.append({"question_idx":2, "answer_idx":11, "text":"오렌지", "desc":"에너지가 느껴지는 상큼하고 신선한 과일향"})
answers.append({"question_idx":2, "answer_idx":12, "text":"사과", "desc":"새콤 달콤한 상쾌한 느낌의 과일향을 좋아하며, "})
answers.append({"question_idx":2, "answer_idx":13, "text":"복숭아", "desc":"향긋하고 달큰한 부드러운 느낌의 과일향을 좋아하며,"})
answers.append({"question_idx":2, "answer_idx":14, "text":"체리", "desc":"달큰하고 진항 사랑스러운 과일향을 좋아하며,"})
answers.append({"question_idx":2, "answer_idx":15, "text":"망고스틴", "desc":"달달하고 은은한 열대과일향을 좋아하며,"})
answers.append({"question_idx":2, "answer_idx":16, "text":"파인애플", "desc":"새콤달콤하고 풍부한 열대과일향을 좋아하며,"})
answers.append({"question_idx":2, "answer_idx":17, "text":"무화과", "desc":"무게감이 느껴지는 달큰한 과일햔을 좋아하며,"})
answers.append({"question_idx":2, "answer_idx":18, "text":"과일향을 좋아하지 않습니다.", "desc":"과일향은 좋아하지 않습니다."})

answers.append({"question_idx":3, "answer_idx":19, "text":"라벤더", "desc":"무게감과 따뜻함이 느껴지는 허브향을 좋아하며,"})
answers.append({"question_idx":3, "answer_idx":20, "text":"캐모마일", "desc":"은은한 과일향이 따뜻하게 느껴지는 허브향을 좋아하며,"})
answers.append({"question_idx":3, "answer_idx":21, "text":"유칼립투스", "desc":"가볍고 시원한 바람같은 허브향을 좋아하며,"})
answers.append({"question_idx":3, "answer_idx":22, "text":"로즈마리", "desc":"신선한 느낌의 묵직한 풀향이 나는 허브향을 좋아하며, "})
answers.append({"question_idx":3, "answer_idx":23, "text":"민트", "desc":"차가운 느낌의 시원한 풀향을 좋아하며,"})
answers.append({"question_idx":3, "answer_idx":24, "text":"이끼식물", "desc":"촉촉한 느낌의 흙향이 풍부한 허브향을 좋아하며,"})
answers.append({"question_idx":3, "answer_idx":25, "text":"수경식물", "desc":"촉촉한 물향과 풀향이 풍부한 식물향을 좋아하며,"})
answers.append({"question_idx":3, "answer_idx":27, "text":"허브향을 좋아하지 않습니다.", "desc":"허브향은 좋아하지 않습니다."})

answers.append({"question_idx":4, "answer_idx":28, "text":"소나무", "desc":"묵직하면서 시원한 소잎향을 좋아하며,"})
answers.append({"question_idx":4, "answer_idx":29, "text":"자작나무", "desc":"깨끗하고 가벼운 느낌의 나무향을 좋아하며,"})
answers.append({"question_idx":4, "answer_idx":30, "text":"송진(미르)", "desc":"섬세하고 향기로우며 따뜻한 나무 수지 향을 좋아하며,"})
answers.append({"question_idx":4, "answer_idx":31, "text":"엠버", "desc":"파우더리 하면서 달큰하고 따뜻한 느낌이 풍부한나무향을 좋아하며,"})
answers.append({"question_idx":4, "answer_idx":32, "text":"가죽", "desc":"단단한 묵직함이 매력젹인 향을 좋아하며, "})
answers.append({"question_idx":4, "answer_idx":33, "text":"머스크", "desc":"아늑하고 포근한 느낌이 드는 파우더리한 향을 좋아하며, "})
answers.append({"question_idx":4, "answer_idx":34, "text":"샌달우드", "desc":"달큰한 느낌이 여성스러운 나무향을 좋아하며,"})
answers.append({"question_idx":4, "answer_idx":35, "text":"숲향을 좋아하지 않습니다.", "desc":"숲향은 좋아하지 않습니다."})


answers.append({"question_idx":5, "answer_idx":36, "text":"커피", "desc":"그리고 씁쓸하면서 무게감 있는 감미로운 향을 좋아합니다."})
answers.append({"question_idx":5, "answer_idx":37, "text":"꿀", "desc":"그리고 진하고 무거운 달달한 향을 좋아합니다."})
answers.append({"question_idx":5, "answer_idx":38, "text":"시나몬", "desc":"그리고 따뜻하고 스파이시한 향신료 향을 좋아합니다."})
answers.append({"question_idx":5, "answer_idx":39, "text":"진저", "desc":"그리고 매콤하고 따뜻한 느낌이 강렬한 향을 좋아합니다."})
answers.append({"question_idx":5, "answer_idx":40, "text":"그린티", "desc":"그리고 은은하고 맑은 차잎향을 좋아합니다."})
answers.append({"question_idx":5, "answer_idx":41, "text":"바닐라", "desc":"그리고 풍부하고 무거운 달큰한 향을 좋아합니다."})
answers.append({"question_idx":5, "answer_idx":42, "text":"초콜렛", "desc":"그리고 진하고 풍부한 담콤한 향을 좋아합니다."})
answers.append({"question_idx":5, "answer_idx":43, "text":"견과류", "desc":"그리고 따뜻하고 건조한 느낌이 동시에 드는 고소한 향을 좋아합니다. "})


db.answers.insert_many(list(answers))
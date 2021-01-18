from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

questions = []
questions.append({"idx":1, "text":"눈을 떠보니 꽃집입니다. 어떤 꽃을 고르시겠어요?"})
questions.append({"idx":2, "text":"눈을 떠보니 카오산로드의 과일 가게입니다. 어떤 과일을 구매 하시겠습니까?"})
questions.append({"idx":3, "text":"눈을 떠보니 허브정원에서 화분을 증정하고 있습니다. 어떤 식물을 가져가시겠습니까?"})
questions.append({"idx":4, "text":"눈을 떠보니 깊숙한 산속입니다.어떤 나무와 동물의 향기가 인상깊으신가요? "})
questions.append({"idx":5, "text":"자, 이제 마지막 여행지 입니다. 눈을 떠보니 바다가 보이는 까페입니다. 마음에 드는 향을 골라보세요."})
db.questions.insert_many(list(questions))

answers = []
answers.append({"question_idx":1, "answer_idx":1, "text":"장미", "desc":"여성스럽고 진한 매혹적인 꽃향"})
answers.append({"question_idx":1, "answer_idx":2, "text":"자스민", "desc":"은은하면서도 우아한 여성미가 풍부한 향"})
answers.append({"question_idx":1, "answer_idx":3, "text":"아카시아", "desc":"청순하고 달달한 꽃향"})
answers.append({"question_idx":1, "answer_idx":4, "text":"라일락", "desc":"청순하고 달달한 꽃향"})
answers.append({"question_idx":1, "answer_idx":5, "text":"은방울", "desc":""})
answers.append({"question_idx":1, "answer_idx":6, "text":"국화", "desc":""})
answers.append({"question_idx":1, "answer_idx":7, "text":"튤립", "desc":""})
answers.append({"question_idx":1, "answer_idx":8, "text":"꽃향을 좋아하지 않습니다.", "desc":""})

answers.append({"question_idx":2, "answer_idx":9, "text":"레몬", "desc":""})
answers.append({"question_idx":2, "answer_idx":10, "text":"자몽", "desc":""})
answers.append({"question_idx":2, "answer_idx":11, "text":"오렌지", "desc":"에너지가 느껴지는 상큼하고 신선한 과일향"})
answers.append({"question_idx":2, "answer_idx":12, "text":"사과", "desc":""})
answers.append({"question_idx":2, "answer_idx":13, "text":"복숭아", "desc":""})
answers.append({"question_idx":2, "answer_idx":14, "text":"체리", "desc":"달큰하고 사랑스러운 과일향"})
answers.append({"question_idx":2, "answer_idx":15, "text":"망고스틴", "desc":""})
answers.append({"question_idx":2, "answer_idx":16, "text":"파인애플", "desc":""})
answers.append({"question_idx":2, "answer_idx":17, "text":"무화과", "desc":""})
answers.append({"question_idx":2, "answer_idx":18, "text":"과일향을 좋아하지 않습니다.", "desc":""})

answers.append({"question_idx":3, "answer_idx":19, "text":"라벤더", "desc":""})
answers.append({"question_idx":3, "answer_idx":20, "text":"캐모마일", "desc":""})
answers.append({"question_idx":3, "answer_idx":21, "text":"유칼립투스", "desc":""})
answers.append({"question_idx":3, "answer_idx":22, "text":"로즈마리", "desc":""})
answers.append({"question_idx":3, "answer_idx":23, "text":"민트", "desc":""})
answers.append({"question_idx":3, "answer_idx":24, "text":"이끼식물", "desc":"이끼와 흙냄새가 올라오는 자연스러운 향"})
answers.append({"question_idx":3, "answer_idx":25, "text":"수경식물", "desc":"싱그러움이 느껴지는 촉촉한 풀향"})

answers.append({"question_idx":4, "answer_idx":26, "text":"소나무", "desc":""})
answers.append({"question_idx":4, "answer_idx":27, "text":"자작나무", "desc":""})
answers.append({"question_idx":4, "answer_idx":28, "text":"송진(미르)", "desc":""})
answers.append({"question_idx":4, "answer_idx":29, "text":"엠버", "desc":""})
answers.append({"question_idx":4, "answer_idx":30, "text":"가죽", "desc":""})
answers.append({"question_idx":4, "answer_idx":31, "text":"머스크", "desc":"이끼와 흙냄새가 올라오는 자연스러운 향"})
answers.append({"question_idx":4, "answer_idx":32, "text":"샌달우드", "desc":"싱그러움이 느껴지는 촉촉한 풀향"})

answers.append({"question_idx":5, "answer_idx":33, "text":"커피", "desc":""})
answers.append({"question_idx":5, "answer_idx":34, "text":"꿀", "desc":""})
answers.append({"question_idx":5, "answer_idx":35, "text":"시나몬", "desc":""})
answers.append({"question_idx":5, "answer_idx":36, "text":"진저", "desc":""})
answers.append({"question_idx":5, "answer_idx":37, "text":"그린티", "desc":""})
answers.append({"question_idx":5, "answer_idx":38, "text":"바닐", "desc":"이끼와 흙냄새가 올라오는 자연스러운 향"})
answers.append({"question_idx":5, "answer_idx":39, "text":"초콜렛", "desc":"싱그러움이 느껴지는 촉촉한 풀향"})
answers.append({"question_idx":5, "answer_idx":40, "text":"견과류", "desc":"싱그러움이 느껴지는 촉촉한 풀향"})


db.answers.insert_many(list(answers))
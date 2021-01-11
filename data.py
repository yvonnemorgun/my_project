from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

questions = []
questions.append({"idx":1, "text":"눈을 떠보니 꽃집입니다. 어떤 꽃을 고르시겠어요?"})
questions.append({"idx":2, "text":"눈을 떠보니 카오산로드의 과일 가게입니다. 어떤 과일을 구매 하시겠습니까?"})
questions.append({"idx":3, "text":"눈을 떠보니 허브정원에서 화분을 증정하고 있습니다. 어떤 식물을 가져가시겠습니까?"})
db.questions.insert_many(list(questions))

answers = []
answers.append({"question_idx":1, "answer_idx":1, "text":"장미", "desc":"정열적이고 매혹적인 꽃향"})
answers.append({"question_idx":1, "answer_idx":2, "text":"자스민", "desc":"은은하면서도 우아한 여성미가 풍부한 향"})
answers.append({"question_idx":1, "answer_idx":3, "text":"아카시아", "desc":"청순하고 달달한 꽃향"})
answers.append({"question_idx":1, "answer_idx":4, "text":"라일락", "desc":"청순하고 달달한 꽃향"})
answers.append({"question_idx":1, "answer_idx":5, "text":"라일락", "desc":""})
answers.append({"question_idx":1, "answer_idx":6, "text":"은방울", "desc":""})
answers.append({"question_idx":1, "answer_idx":7, "text":"국화", "desc":""})
answers.append({"question_idx":1, "answer_idx":8, "text":"튤립", "desc":""})
answers.append({"question_idx":1, "answer_idx":9, "text":"꽃향을 좋아하지 않습니다.", "desc":""})

answers.append({"question_idx":2, "answer_idx":10, "text":"레몬", "desc":""})
answers.append({"question_idx":2, "answer_idx":11, "text":"자몽", "desc":""})
answers.append({"question_idx":2, "answer_idx":12, "text":"오렌지", "desc":"에너지가 느껴지는 상큼하고 신선한 과일향"})
answers.append({"question_idx":2, "answer_idx":13, "text":"사과", "desc":""})
answers.append({"question_idx":2, "answer_idx":14, "text":"복숭아", "desc":""})
answers.append({"question_idx":2, "answer_idx":15, "text":"체리", "desc":"달큰하고 사랑스러운 과일향"})
answers.append({"question_idx":2, "answer_idx":16, "text":"망고스틴", "desc":""})
answers.append({"question_idx":2, "answer_idx":17, "text":"파인애플", "desc":""})
answers.append({"question_idx":2, "answer_idx":18, "text":"무화과", "desc":""})
answers.append({"question_idx":2, "answer_idx":19, "text":"과일향을 좋아하지 않습니다.", "desc":""})

answers.append({"question_idx":3, "answer_idx":20, "text":"라벤더", "desc":""})
answers.append({"question_idx":3, "answer_idx":21, "text":"캐모마일", "desc":""})
answers.append({"question_idx":3, "answer_idx":22, "text":"유칼립투스", "desc":""})
answers.append({"question_idx":3, "answer_idx":23, "text":"로즈마리", "desc":""})
answers.append({"question_idx":3, "answer_idx":24, "text":"민트", "desc":""})
answers.append({"question_idx":3, "answer_idx":25, "text":"이끼식물", "desc":"이끼와 흙냄새가 올라오는 자연스러운 향"})
answers.append({"question_idx":3, "answer_idx":26, "text":"수경식물", "desc":"싱그러움이 느껴지는 촉촉한 풀향"})

db.answers.insert_many(list(answers))

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm


# Create your views here.
def index(request):

    lottos = GuessNumbers.objects.all()

    return render(request, 'lotto/default.html', {'lottos':lottos})

    # user_input_name = request.POST['name']
    # user_input_text = requets.POST['text']
    #
    # new_row = GuessNumbers(name=user_input_name, text=user_input_text)
    #
    # print(new_row.num_lotto)
    # print(new_row.name)
    #
    # new_row.name = new_ros.name.upper()
    #
    ##new_row.generate()

    # new_row.lottos = ""
    # origin = list(range(1,46)) # 1~45의 숫자 리스트 [1, 2, 3, ..., 43, 44, 45]
    # # 6개 번호 set 갯수만큼 1~46 뒤섞은 후 앞의 6개 골라내어 sorting
    # for _ in range(0, new_row.num_lotto):
    #     random.shuffle(origin) # [10, 21, 36, 2, ... , 1, 11]
    #     guess = origin[:6] # [10, 21, 36, 2, 15, 23]
    #     guess.sort() # [2, 10, 15, 21, 23, 36]
    #     self.lottos += str(guess) +'\n' # 로또 번호 str에 6개 번호 set 추가 -> '[2, 10, 15, 21, 23, 36]\n'
    #     # self.lottos : '[2, 10, 15, 21, 23, 36]\n[1, 15, 21, 27, 30, 41]\n...'
    # new_row.update_date = timezone.now()
    # new_row.save() # GuessNumbers object를 DB에 저장
    #
    # # new_row.lottos = [np.randint(1,50) for i in range(6)]


    #return HttpResponse('<h1>Hello, World</h1>')

def post(request):


    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()

            return redirect('index')

        # print(type(lotto))
        # print(lotto)

        # print(type(form))
        # print(form)

        # print(request.POST['name'])
        # print(request.POST['text'])
    else:
        form = PostForm()
        return render(request, "lotto/form.html", {"form":form})



def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, World</h1>")



def detail(request, lottokey):

    lotto = GuessNumbers.objects.get(id=lottokey)

    return render(request, "lotto/detail.html", {"lotto":lotto})

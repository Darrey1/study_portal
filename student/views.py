from django.shortcuts import render,redirect
from .forms import Note_Form, Todo_form,homework_Form,Books,Login_Form,Register,Reset_Pass
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Notes, Todo,Homework
from django.contrib.auth.decorators import login_required
from .date import get_date
from youtubesearchpython import  VideosSearch
import requests
import wikipedia
# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def notes(request):
    note = Notes.objects.filter(user=request.user)
    if len(note) == 0:
        note_finished = True
    else:
        note_finished = False
    return render(request,'notes.html', {'notes':note, 'finished':note_finished})


def create_note(request):
     if request.method == 'POST':
        form = Note_Form(request.POST)
        if form.is_valid():
            note = Notes(user=request.user,
                         title = request.POST['title'],
                         author = request.POST['author'],
                         description = request.POST['description'],
                         created_at = request.POST['created_at']
                         )
            note.save()
        return redirect('notes')
     else:
        form = Note_Form()
     return render(request, 'form.html', {'form':form})
 
 
def delete_note(request, pk=None):
    note = Notes.objects.get(id=pk)
    note.delete()
    return redirect('notes')


def note_del_confr(request, pk=None):
    note = Notes.objects.get(id=pk)
    return render(request, 'delete.html', {'note':note})


def edit_note(request, pk=None):
    note = Notes.objects.get(id=pk)
    if request.method == 'POST':
        form = Note_Form(request.POST)
        if form.is_valid():
            note.title = request.POST['title']
            note.author = request.POST['author']
            note.description = request.POST['description']
            note.created_at = request.POST['created_at']
        note.save()
        return redirect('notes')
    else:
        form = Note_Form()
    return render(request, 'form.html', {'form':form, 'note':note})


def note_details(request, pk=None):
    details = Notes.objects.get(id=pk)
    return render(request,'notes_detail.html', {'detail':details})


# todo
@login_required
def todo(request):
    todo_info = Todo.objects.filter(user=request.user)
    if len(todo_info) == 0:
        todo_finished = True
    else:
        todo_finished = False
    today = get_date()
    return render(request, 'todo.html', {'infos':todo_info, 'today':today, 'finished':todo_finished})


def create_todo(request):
    if request.method == 'POST':
        todo_form = Todo_form(request.POST)
        if todo_form.is_valid():
            try:
               finished = request.POST['status']
               if finished == 'on':
                   is_finished = True
               else:
                   is_finished = False
            except:
                is_finished = False
            create = Todo(user=request.user,
                          title = request.POST['title'],
                          due_date = request.POST['due_date'],
                          status = is_finished
                          )
            create.save()
        return redirect('todo')
    else:
        todo_form = Todo_form()
    return render(request, 'form.html', {'form':todo_form})


def update_status(request, pk=None):
    update= Todo.objects.get(id=pk)
    #if request.method == 'POST':
    if update.status == True:
        update.status = False
    else:
        update.status = True
    update.save()
    return redirect('todo')
def delete_todo(request, pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect('todo')
def delete_conf(request, pk=None):
    delete = Todo.objects.get(id=pk)
    return render(request, 'delete1.html', {'note':delete})
def edit_todo(request, pk=None):
    edit = Todo.objects.get(id=pk)
    if request.method == 'POST':
       form = Todo_form(request.POST)
       if form.is_valid():
           try:
              status = request.POST['status']
              if status == True:
                  status = False
              else:
                  status = True
           except:
               status = False
           
           edit.title = request.POST['title']
           edit.due_date = request.POST['due_date']
           edit.status = status
       edit.save()
       return redirect('todo')
    else:
        form = Todo_form()
    return render(request, 'form.html', {'form':form})

# homework
@login_required
def homework(request):
    homework = Homework.objects.filter(user=request.user)
    today = get_date()
    print(today)
    print(type(today))
    try:
       if len(homework) == 0:
           homework_done = True
       else:
           homework_done = False
    except:
        homework_done = False
    return render(request, 'homework.html', {'homeworks':homework, 'homework_done':homework_done, 'today':today})
def create_homework(request):
    if request.method == 'POST':
        homework = homework_Form(request.POST)
        if homework.is_valid():
            try:
               status = request.POST['status']
               if status == 'on':
                   is_status = True
               else:
                   is_status = False
            except:
                is_status = False
            home = Homework(user=request.user,
                        subject = request.POST['subject'],
                        title = request.POST['title'],
                        description = request.POST['description'],
                        due_date = request.POST['due_date'],
                        status =is_status
                        )
            home.save()
        return redirect('homework')
    else:
        homework = homework_Form()
    return render(request, 'form.html',{'form':homework})
def update_homework(request, pk):
    update = Homework.objects.get(id=pk)
    #if request.method == 'POST':
    try:
      if update.status == True:
          is_status = False
      else:
          is_status = True
    except:
        is_status = True
    update.status = is_status
    update.save()
    return redirect('homework')
def delete_homework(request, pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect('homework')
def homework_conf(request, pk=None):
    conf = Homework.objects.get(id=pk)
    return render(request, 'delete3.html', {'homework':conf})
def homework_details(request, pk):
    detail = Homework.objects.get(id=pk)
    return render(request, 'homeworkdetails.html', {'detail':detail})

# youtube
@login_required
def youtube(request):
    if request.method == 'POST':
        form = Books(request.POST)
        if form.is_valid():
            text = request.POST['search']
            videosSearch = VideosSearch(text, limit = 11)
            lists = []
            try:
               error = ''
               for i in videosSearch.result()["result"]:
                   data = {
                       'title':i["title"],
                       'channel':i["channel"].get("name"),
                       'duration':i["accessibility"].get("duration"),
                       'views':i["viewCount"].get("short"),
                       'publish':i["publishedTime"],
                       #'description':i["descriptionSnippet"][0].get("text"),
                       'link':i["link"],
                       'thumbnail':i["thumbnails"][0].get("url")
                   }
                   description = ''
                   if i["descriptionSnippet"]:
                      for j in i["descriptionSnippet"]:
                          description += j["text"]
                          data['description'] = description
                       
                   lists.append(data)
            except Exception as arr:
                #form=form
                form = form
                error = arr
            return render(request, 'youtube.html', {'form':form, 'lists':lists, 'error':error})
    else:
        form = Books()
        lists = []
        error = ''
    return render(request, 'youtube.html', {'form':form, 'lists':lists, 'error':error})
@login_required
def books(request):
    if request.method == 'POST':
        try:
           lists = []
           form = Books(request.POST)
           if form.is_valid():
              text = request.POST['search']
              url = "https://www.googleapis.com/books/v1/volumes?q="+text
              data = requests.get(url)
              answer = data.json()
              error = ''
              for i in range(10):
                    data_list = {
                     'title':answer['items'][i]["volumeInfo"]['title'],
                     'subtitle':answer['items'][i]["volumeInfo"].get('subtitle'),
                     'rating':answer['items'][i]["volumeInfo"].get('ratingsCount'),
                     'category': answer['items'][i]["volumeInfo"].get('categories')[0],
                     'page_count':answer['items'][i]["volumeInfo"].get('pageCount'),
                     'link':answer['items'][i]["volumeInfo"].get('previewLink'),
                     'description': answer['items'][i]["volumeInfo"].get('description'),
                     'image':answer['items'][i]["volumeInfo"].get("imageLinks").get('thumbnail')
                    }
                    #data_list['clean_category'] =data_list['category']
                    lists.append(data_list)
        except TypeError:
                for i in range(2):
                    data_list = {
                     'title':answer['items'][i]["volumeInfo"]['title'],
                     'subtitle':answer['items'][i]["volumeInfo"].get('subtitle'),
                     'rating':answer['items'][i]["volumeInfo"].get('ratingsCount'),
                     'category': answer['items'][i]["volumeInfo"].get('categories')[0],
                     'page_count':answer['items'][i]["volumeInfo"].get('pageCount'),
                     'link':answer['items'][i]["volumeInfo"].get('previewLink'),
                     'description': answer['items'][i]["volumeInfo"].get('description'),
                     'image':answer['items'][i]["volumeInfo"].get("imageLinks").get('thumbnail')
                    }
                    #data_list['clean_category'] =data_list['category']
                    lists.append(data_list)
        except requests.exceptions.ConnectionError as arr:
            form = form
            error = 'connection error,Please check your internet connection and try again'
            pass
        except requests.exceptions.RequestException as arr:
             form = form
             error = arr
             pass
        except:
             form = form
             error =  f'An error occur while searching for {text},Please try again.'
        return render(request, 'books.html', {'lists':lists,'form':form,'error':error})
    else:
        form = Books()
        lists = []
        error = ''
    return render(request, 'books.html', {'lists':lists,'form':form,'error':error})
    
# dictionary 
@login_required
def dictionary(request):
    if request.method == "POST":
        form = Books(request.POST)
        text = request.POST['search']
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        print(url)
        r = requests.get(url)
        answer = r.json()
        try:
           phonetics = answer[0]['phonetics'][0]['text']
           audio = answer[0]['phonetics'][0]['audio']
           definition = answer[0]['meanings'][0]['definitions'][0]['definition']
           Class = answer[0]['meanings'][0]["partOfSpeech"]
           synonyms = answer[0]['meanings'][0]['definitions'][0]['synonyms']
           context = {
               'form':form,
               'input':text,
               'phonetics':phonetics,
               'audio':audio,
               'definition':definition,
               'example':Class,
               'synonyms':synonyms,
               'error':''
           }
        
        except IndexError:
            definition = answer[0]['meanings'][0]['definitions'][0]['definition']
            Class = answer[0]['meanings'][0]["partOfSpeech"]
            synonyms = answer[0]['meanings'][0]['definitions'][0]['synonyms']
            context ={
            'form':form,
            'example':Class,
            'synonyms':synonyms,
            'definition':definition,
            'input': text,
            'error':''
            
            }
        except KeyError as arr:
            context ={
                'form':form,
            'input': text,
             'error':arr
             }
        except requests.exceptions.ConnectionError as arr:
             context ={
            'input': text,
            'error':'ConnectionError'
             }
            
        except requests.exceptions.RequestException as arr:
             context ={
            'input': text,
             'error':arr
             }
        except Exception as arr:
            context = {
                'form':form,
                'error':arr,
                'input':text
            }
        except:
            definition = answer[0]['meanings'][0]['definitions'][0]['definition']
            Class = answer[0]['meanings'][0]["partOfSpeech"]
            synonyms = answer[0]['meanings'][0]['definitions'][0]['synonyms']
            context ={
            'form':form,
            'example':Class,
            'synonyms':synonyms,
            'definition':definition,
            'input': text,
            'error':''
                
            
           }
        return render(request,"dictionary.html",context)
        
    else:
        form = Books()
        context = {'form':form}
    return render(request,"dictionary.html",context)
# wikipedia
@login_required
def wiki(request):
    if request.method == 'POST':
        try:
           text = request.POST['search']
           form = Books(request.POST)
           pass
           search = wikipedia.page(text)
           context = {
               'form':form,
               'title':search.title,
               'link':search.url,
               'details':search.summary,
               'error': ''
           }
           return render(request,"wiki.html",context)
        except Exception as arr:
            context = {
                'error': arr
            }
            
    else:
        form = Books()
        context = {
            'form':form,
            'error':''
        }
    return render(request,"wiki.html",context)
# conversion
@login_required
def conversion(request):
    return render(request, 'conversion.html')

# registration
def registration(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            username = request.POST['username']
            username = str(username).capitalize()
            email = request.POST['email']
            password = request.POST['password']
            confirm = request.POST['confirm_password']
            if password == confirm:
                if User.objects.filter(username=username).exists():
                    message = f'*{str(username).capitalize()} already been used'
                elif User.objects.filter(email=email).exists():
                    message = f'*{email} already been used'
                else:
                   user = User.objects.create_user(username,email, password) 
                   user.save() 
                   return redirect('login')
            else:
                message = '*The two password doesn\'t match'
        return render(request, 'register.html',{'form':form, 'message':message}) 
    else:
        form = Register()
        return render(request, 'register.html',{'form':form})
#sign in
def login_(request):
    if request.method == 'POST':
        form = Login_Form(request.POST)
        if form.is_valid():
            username = request.POST['username']
            username = str(username).capitalize()
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            #elif user.username not in user:
            #    pass
            else:
                message = '*Invalid Crediential!'
                form = AuthenticationForm()
            return render(request, 'login.html', {'form':form, 'message':message})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

#logout
def user_logout(request):
    logout(request)
    return redirect('home')
def confirm_logout(request):
    return render(request, 'delogout.html')

#password reset form
def reset_password(request):
    if request.method == 'POST':
        form = Reset_Pass(request.POST)
        if form.is_valid():
            username = request.POST['Former_username']
            password = request.POST['new_password']
            confirm_password = request.POST['confirm_pass']
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                   user = User.objects.get(username=username)
                   user.set_password(password)
                   user.save()
                   return redirect('login')
                else:
                    message = f'*{username} doesn\'t exist,enter your account username'
            else:
                message ='*The two password doesn\'t match'
        return render(request, 'reset.html', {'form':form, 'message':message})
    else:
        form = Reset_Pass()
        return render(request, 'reset.html', {'form':form})
    
# end 
            
            
                    


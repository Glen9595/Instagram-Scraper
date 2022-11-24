import instaloader #For Instagram Connection
import hashlib #For Hashing Algorythms
from datetime import datetime #For Time Conversion
import colorama
from colorama import Fore, Style
from stringhe import * 
import ntplib
from time import ctime
import os
import shutil
import glob
import pandas as pd
import orjson 

USER=''
name = ""
nickname = ''

colorama.init(autoreset='true')                     

c = ntplib.NTPClient()
response = c.request('it.pool.ntp.org')

print(f"{Fore.GREEN}{Style.BRIGHT}"+t0)
print(f"{Fore.GREEN}{Style.BRIGHT}"+t1)
print(f"{Fore.GREEN}{Style.BRIGHT}"+t2)
print(te1)
print(f"{Fore.BLUE}{Style.BRIGHT}"+p1)
print(te2)
print(f"{Fore.CYAN}{Style.BRIGHT}"+s1) 
USER = input("")
print(f"{Fore.GREEN}{Style.BRIGHT}"+spazio1)

L = instaloader.Instaloader(download_comments=True, save_metadata=True, compress_json=False) #Creation of connection to instagram

app_logs = ""
all_received_data = ""
completepath =""

# Get Data from user
def input_data():
    print(f"{Fore.BLUE}{Style.BRIGHT}"+p2)
    print(f"{Fore.CYAN}{Style.BRIGHT}"+s2) 
    user_nickname = input("")
    print(f"{Fore.GREEN}{Style.BRIGHT}"+spazio1)
    print(f"{Fore.MAGENTA}{Style.BRIGHT}"+s3) 
    print(te4)
    print(te8)
    print(te9)
    print(te10)
    print(te11)
    print(f"{Fore.MAGENTA}{Style.BRIGHT}"+s5)
    print(te12)
    print(te13)
    print(te15)   
    print(f"{Fore.CYAN}{Style.BRIGHT}"+s6) 
    required_data = input("").split()

    return user_nickname, required_data



def hash():
    
    shafinale=pd.DataFrame(columns=[])
    filenames = glob.glob("**")

    for filename in filenames:
        with open(filename, 'rb') as inputfile:
            data = inputfile.read()
            filename=inputfile.name
            s256 = hashlib.sha256(data).hexdigest()
            


            s512 = hashlib.sha512(data).hexdigest()
            minedata2={'filename':filename,'Sha256':s256, 'Sha512':s512}
            minedata3=pd.DataFrame(minedata2,index=[0])
            shafinale=pd.concat([shafinale,minedata3],ignore_index=True)
    shafinale.to_csv('Hash.csv', sep=';')
    

    


def comments():
    
    
    dataframe2 = pd.DataFrame(columns=[])
     
    for file in glob.glob('*comments.json'):
        with open(file, 'r') as filecontent:
            filename = filecontent.name
                     
    # Process each file here
            df = pd.read_json(file)
            df.to_csv(filename+'.csv', sep=';')



def parser_tagged(username, path,contex):

    #print('Entering provided directory...')
    os.chdir(os.path.join(path, '@'+username+contex))
    
    columns = ['filename', 'datetime', 'video_duration']  
    dataframe = pd.DataFrame(columns=[])
    #print('Traversing file tree...')
    
#glob('*UTC.json')
    
    for file in glob.glob('*UTC.json'):
        with open(file, 'r') as filecontent:
            filename = filecontent.name
            #print('Found JSON file: ' + filename + '. Loading...')
            
            try:
                metadata = orjson.loads(filecontent.read())
            
            except IOError as e:
                #print("I/O Error. Couldn't load file. Trying the next one...")
                continue
            else:
                pass
            #print('Collecting relevant metadata...')
            time = datetime.fromtimestamp(int(metadata['node']['taken_at_timestamp']))
            username = metadata['node']['owner']['id']
            try:
                post_id = metadata['node']['id']
            except:
                post_id = ""
            minedata = {'filename': filename, 'time': time, 'username_id' : username,   'post_id' : post_id}
            minedata2=pd.DataFrame(minedata,index=[0])
            #print('Writing to dataframe...')
            dataframe=pd.concat([dataframe,minedata2],ignore_index=True)
            print(dataframe)
            #print('Closing file...')
            del metadata
            filecontent.close()
    #print('Storing dataframe to CSV file...')
    #print('Done.')
    dataframe['source'] = 'Instagram'
    return dataframe





def parser_stories(username, path,contex):

    #print('Entering provided directory...')
    os.chdir(os.path.join(path, '@'+username+contex))
    
    columns = ['filename', 'datetime', 'video_duration']  
    dataframe = pd.DataFrame(columns=[])
    #print('Traversing file tree...')
    
#glob('*UTC.json')
    
    for file in glob.glob('*UTC.json'):
        with open(file, 'r') as filecontent:
            filename = filecontent.name
            #print('Found JSON file: ' + filename + '. Loading...')
            
            try:
                metadata = orjson.loads(filecontent.read())
            
            except IOError as e:
                #print("I/O Error. Couldn't load file. Trying the next one...")
                continue
            else:
                pass
            #print('Collecting relevant metadata...')
            time = datetime.fromtimestamp(int(metadata['node']['taken_at_timestamp']))
            username = metadata['node']['owner']['username']
            try:
                post_id = metadata['node']['id']
            except:
                post_id = ""
            minedata = {'filename': filename, 'time': time, 'username' : username,   'post_id' : post_id}
            minedata2=pd.DataFrame(minedata,index=[0])
            #print('Writing to dataframe...')
            dataframe=pd.concat([dataframe,minedata2],ignore_index=True)
            print(dataframe)
            #print('Closing file...')
            del metadata
            filecontent.close()
    #print('Storing dataframe to CSV file...')
    #print('Done.')
    dataframe['source'] = 'Instagram'
    return dataframe


#parser 
def parse_instafiles(username, path,contex):
    """ 
    This function loads in all the json files generated by the instaloader package and parses it into a csv file.
    """
    #print('Entering provided directory...')
    os.chdir(os.path.join(path, '@'+username+contex))
    
    columns = ['filename', 'datetime', 'type', 'locations_id', 'locations_name', 'mentions', 'hashtags', 'video_duration']
    
    dataframe = pd.DataFrame(columns=[])
    
    #print('Traversing file tree...')
    
#glob('*UTC.json')
    
    for file in glob.glob('*UTC.json'):
        with open(file, 'r') as filecontent:
            filename = filecontent.name
            #print('Found JSON file: ' + filename + '. Loading...')
            
            try:
                metadata = orjson.loads(filecontent.read())
            
            except IOError as e:
                #print("I/O Error. Couldn't load file. Trying the next one...")
                continue
            else:
                pass
            #print('Collecting relevant metadata...')
            time = datetime.fromtimestamp(int(metadata['node']['taken_at_timestamp']))
            type_ = metadata['node']['__typename']
            likes = metadata['node']['edge_media_preview_like']['count']     
            comments = metadata['node']['edge_media_to_comment']['count']
            username = metadata['node']['owner']['username']
            followers = metadata['node']['owner']['edge_followed_by']['count']
            try:
                text = metadata['node']['edge_media_to_caption']['edges'][0]['node']['text']
            except:
                text = ""
            try:
                post_id = metadata['node']['id']
            except:
                post_id = ""
            minedata = {'filename': filename, 'time': time, 'text': text,
                    'likes': likes, 'comments' : comments, 'username' : username,  'followers' : followers, 'post_id' : post_id}
            #print('Writing to dataframe...')
            minedata2=pd.DataFrame(minedata,index=[0])
            dataframe=pd.concat([dataframe,minedata2],ignore_index=True)
            print(dataframe)
            #print('Closing file...')
            del metadata
            filecontent.close()
    #print('Storing dataframe to CSV file...')
    #print('Done.')
    dataframe['source'] = 'Instagram'
    return dataframe

# Data Hashing
def double_hash_system(data_to_hash, sname, nn, cpath):
    datatohash = data_to_hash.encode()

    #First Hashing
    sha256 = hashlib.sha256(datatohash).hexdigest()

    #Second Hashing
    sha512 = hashlib.sha512(datatohash).hexdigest()

    return sha256, sha512, sname, nn, cpath


# Data evaluation
def look_for_data():
    global app_logs, all_received_data, name, nickname, completepath

    app_logs += "\nGetting data from user... " + (ctime(response.tx_time)) + " from server ntp: 0.it.pool.ntp.org"
    nickname, data = input_data()
    app_logs += "\nUser data collected succesfully! " + (ctime(response.tx_time)) + " from server ntp: 0.it.pool.ntp.org"

    app_logs += "\nStarting scrapping library... " + (ctime(response.tx_time))  + " from server ntp: 0.it.pool.ntp.org"
    profile = instaloader.Profile.from_username(L.context, nickname)
    app_logs += "\nScrapping library started successfully! " + (ctime(response.tx_time))  + " from server ntp: 0.it.pool.ntp.org"
    
    app_logs += "\nPrinting data to user... " + (ctime(response.tx_time))  + " from server ntp: 0.it.pool.ntp.org"
    print('\n\n\nDATA:\n')
    for el in data:
        if el == "profileinfo":          
            name = 'Profile Info:\n'
            all_received_data +="\t\t@" + nickname + "\n"
            print(f"{Fore.GREEN}{Style.BRIGHT}"+g1, (str(profile.biography)))
            all_received_data += ' bio: '+str(profile.biography)+', '
            print(f"{Fore.GREEN}{Style.BRIGHT}"+g2, str(profile.followers))
            all_received_data += ' followers: '+str(profile.followers)+', '
            print(f"{Fore.GREEN}{Style.BRIGHT}"+g4, str(profile.followees))
            all_received_data += ' following: '+str(profile.followees)+', '
            print(f"{Fore.GREEN}{Style.BRIGHT}"+g3, str(profile.mediacount))
            all_received_data += ' mediacount: '+str(profile.mediacount)+', '
            completepath= '@'+ nickname + "-profile/"
            completename= "profileinfo.txt"
            if not os.path.exists(completepath):
                os.makedirs(completepath)
            with open(os.path.join(completepath, completename), 'w') as f:
                f.write(all_received_data)
            os.chdir(completepath)

        elif el == "posts":
            name = 'Posts:\n'
            print(f"{Fore.GREEN}{Style.BRIGHT}"+g5 + nickname + "-posts... ")
            if "timeperiod" not in data:
                for post in profile.get_posts():
                    print(post)
                    if "metadata" in data:
                        print(f"{Fore.CYAN}{Style.BRIGHT}"+inf)
                        try:
                            print(f"{Fore.YELLOW}{Style.BRIGHT}"+g6, str(post.likes))
                            print(f"{Fore.YELLOW}{Style.BRIGHT}"+g7, str(post.date))
                            print(f"{Fore.YELLOW}{Style.BRIGHT}"+g8, str(post.caption))
                            print(f"{Fore.YELLOW}{Style.BRIGHT}"+g9, str(post.tagged_users))
                            print(f"{Fore.YELLOW}{Style.BRIGHT}"+g10, str(post.location))
                        except Exception:
                           print(f"{Fore.RED}{Style.BRIGHT}"+r1)
                    
                    target_name_download = '@' + nickname + '-posts'
                    completepath = '@' + nickname + '-posts'
                    L.download_post(post, target=target_name_download)
                    
                df_instagram = parse_instafiles(nickname, os.getcwd(),'-posts' )
                df_instagram.to_csv("metadati_compressi.csv",sep=';')
                comments()
                    
            elif "timeperiod" in data:
                
                print("Effettua il download di file solo in uno specifico intervallo temporale, secondo il formato 'aaaa mm gg'")
                print("\nesempio data inizio periodo: 2015 12 1")
                print("esempio data fine periodo: 2022 9 26")
                try:
                    since_year, since_month, since_day = [int(el) for el in input("\nInserisci la data di INIZIO periodo: ").split()]
                    until_year, until_month, until_day = [int(el) for el in input("Inserisci la data di FINE periodo: ").split()]
                    print('\n')
                except Exception:
                    print("Hai inserito un valore errato.\nPuoi tentare di nuovo rispettando il formato 'aaaa mm gg'\n")
                    since_year, since_month, since_day = [int(el) for el in input("Inserisci la data di INIZIO periodo: ").split()]
                    until_year, until_month, until_day = [int(el) for el in input("Inserisci la data di FINE periodo: ").split()]
                    print('\n')
                SINCE = datetime(since_year, since_month, since_day)
                UNTIL = datetime(until_year, until_month, until_day)

                k = 0

                for post in profile.get_posts():
                    postdate = post.date

                    if postdate > UNTIL:
                        continue
                    elif postdate <= SINCE:
                        k += 1
                        if k == 50:
                            break
                        else:
                            continue
                    else:

                        if "metadata" in data:
                            print(f"{Fore.CYAN}{Style.BRIGHT}"+inf)
                            try:
                                print(f"{Fore.YELLOW}{Style.BRIGHT}"+g6, str(post.likes))
                                print(f"{Fore.YELLOW}{Style.BRIGHT}"+g7, str(post.date))
                                print(f"{Fore.YELLOW}{Style.BRIGHT}"+g8, str(post.caption))
                                print(f"{Fore.YELLOW}{Style.BRIGHT}"+g9, str(post.tagged_users))
                                print(f"{Fore.YELLOW}{Style.BRIGHT}"+g10, str(post.location))
                            except Exception:
                                print(f"{Fore.RED}{Style.BRIGHT}"+r1)

                        target_name_download = '@' + nickname + '-posts'
                        completepath = '@' + nickname + '-posts'
                        L.download_post(post, target=target_name_download)
                        

                        k = 0
                
                df_instagram = parse_instafiles(nickname, os.getcwd(),'-posts' )
                df_instagram.to_csv("metadati_compressi.csv", sep=';')
                comments()
        
       
        elif el == "stories":
            name = 'Stories:\n'
            print(f"{Fore.GREEN}{Style.BRIGHT}"+g12) 
            profile_of_interest_id = L.check_profile_id(nickname)
            user_id = [profile_of_interest_id]
            L.download_stories(userids=user_id, filename_target='{}'.format('@'+ profile.username + "-stories"))  
            completepath = '@' + nickname + '-stories'
            all_received_data='ciao'
            df_instagram=parser_stories(nickname, os.getcwd(),'-stories')
            df_instagram.to_csv('metadati_compressi.csv', sep=';')


        elif el == "hl":
            print(f"{Fore.GREEN}{Style.BRIGHT}"+g13) 
            for highlight in L.get_highlights(profile):
                print(highlight)
                for item in highlight.get_items():
                    print(item)

                    if "metadata" in data:
                        print(f"{Fore.CYAN}{Style.BRIGHT}"+inf)
                        try:
                            print(f"{Fore.YELLOW}{Style.BRIGHT}"+g14, str(highlight.title))
                            print(f"{Fore.YELLOW}{Style.BRIGHT}"+g15, str(highlight.cover_url))
                               
                        except Exception:
                            print(f"{Fore.RED}{Style.BRIGHT}"+r1)

                    L.download_storyitem(item, '{}'.format('@'+profile.username+'-highlights'))
                name = 'Highlight: '+ highlight.title + '\n'
            
                completepath = '@'+profile.username+'-highlights'
                df_instagram=parser_stories(nickname, os.getcwd(),'-highlights')
                df_instagram.to_csv('metadati_compressi.csv', sep=';')

        elif el == "tagged":
            name = "Tagged Posts:\n"
            print(f"{Fore.GREEN}{Style.BRIGHT}"+g11 + nickname + "-tagged... ") 
            if "timeperiod" not in data:
                for post in profile.get_tagged_posts():
                    print(post)

                    if "metadata" in data:
                        print(f"{Fore.CYAN}{Style.BRIGHT}"+inf)
                        try:
                            print(f"{Fore.YELLOW}{Style.BRIGHT}"+g6, str(post.likes))
                            print(f"{Fore.YELLOW}{Style.BRIGHT}"+g7, str(post.date))
                            print(f"{Fore.YELLOW}{Style.BRIGHT}"+g8, str(post.caption))
                            print(f"{Fore.YELLOW}{Style.BRIGHT}"+g9, str(post.tagged_users))
                            print(f"{Fore.YELLOW}{Style.BRIGHT}"+g10, str(post.location))
                        except Exception:
                            print(f"{Fore.RED}{Style.BRIGHT}"+r1)

                    target_name_download = '@' + nickname + '-tagged'

                    L.download_post(post, target=target_name_download)
                    completepath = '@' + nickname + '-tagged'


                df_instagram=parser_tagged(nickname, os.getcwd(),'-tagged')   
                df_instagram.to_csv("metadati_compressi.csv", sep=';')
                comments()

            elif "timeperiod" in data:
                
                print("Effettua il download di file solo in uno specifico intervallo temporale, secondo il formato 'aaaa mm gg'")
                print("\nesempio data inizio periodo: 2015 12 1")
                print("esempio data fine periodo: 2022 9 26")
                try:
                    since_year, since_month, since_day = [int(el) for el in input("\nInserisci la data di INIZIO periodo: ").split()]
                    until_year, until_month, until_day = [int(el) for el in input("Inserisci la data di FINE periodo: ").split()]
                    print('\n')
                except Exception:
                    print("Hai inserito un valore errato.\nPuoi tentare di nuovo rispettando il formato 'aaaa mm gg'\n")
                    since_year, since_month, since_day = [int(el) for el in input("Inserisci la data di INIZIO periodo: ").split()]
                    until_year, until_month, until_day = [int(el) for el in input("Inserisci la data di FINE periodo: ").split()]
                    print('\n')
                SINCE = datetime(since_year, since_month, since_day)
                UNTIL = datetime(until_year, until_month, until_day)

                k = 0

                for post in profile.get_tagged_posts():
                    postdate = post.date

                    if postdate > UNTIL:
                        continue
                    elif postdate <= SINCE:
                        k += 1
                        if k == 50:
                            break
                        else:
                            continue
                    else:
                        if "metadata" in data:
                            print(f"{Fore.CYAN}{Style.BRIGHT}"+inf)
                            try:
                                print(f"{Fore.YELLOW}{Style.BRIGHT}"+g6, str(post.likes))
                                print(f"{Fore.YELLOW}{Style.BRIGHT}"+g7, str(post.date))
                                print(f"{Fore.YELLOW}{Style.BRIGHT}"+g8, str(post.caption))
                                print(f"{Fore.YELLOW}{Style.BRIGHT}"+g9, str(post.tagged_users))
                                print(f"{Fore.YELLOW}{Style.BRIGHT}"+g10, str(post.location))
                            except Exception:
                                print(f"{Fore.RED}{Style.BRIGHT}"+r1)

                        target_name_download = '@' + nickname + '-tagged'
                        completepath = '@' + nickname + '-tagged'
                        L.download_post(post, target=target_name_download)
                        k = 0
                df_instagram=parser_tagged(nickname, os.getcwd(),'-tagged')   
                df_instagram.to_csv("metadati_compressi.csv", sep=';')
                comments()
    app_logs += "\nSuccesfully printed data to user! " + (ctime(response.tx_time))  + " from server ntp: 0.it.pool.ntp.org"

# App Build and Work
def app():
    prompt='S'
    pathI=os.getcwd()
    while prompt=='S':
        global app_logs, all_received_data, name, nickname, USER

        app_logs += "\nStarting App " + (ctime(response.tx_time))  + " from server ntp: 0.it.pool.ntp.org"
        app_logs += "\nApp started succesfully! " + (ctime(response.tx_time))  + " from server ntp: 0.it.pool.ntp.org"    
        
        app_logs += "\nPersonal Account LogIn Procedure Started... " + (ctime(response.tx_time))  + " from server ntp: 0.it.pool.ntp.org" 
        L.load_session_from_file(USER)
        app_logs += "\nPersonal Account LogIn Procedure Completed!" + (ctime(response.tx_time))  + " from server ntp: 0.it.pool.ntp.org"

        # Get Data
        look_for_data()

        
        # Double Hashing Algorythm
        hash()
        os.chdir(pathI)
        app_logs += "\nLogs wrote succesfully! " + (ctime(response.tx_time))  + " from server ntp: 0.it.pool.ntp.org"
        app_logs += "\nClosing App... " + (ctime(response.tx_time))  + " from server ntp: 0.it.pool.ntp.org"

        # Print logs into .txt file
        with open('instagramscraper_apploggs.txt', 'w') as f:
            f.write(app_logs)

                # filtro cartelle
        print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}"+path)
        percorso = input("") 
        
        source = os.path.dirname(os.path.realpath(__file__))
        if percorso != "":
            # gather all files
            
            allfiles = glob.glob(os.path.join(pathI, '*@*'), recursive=True)
            print(f"{Fore.GREEN}{Style.BRIGHT}"+spazio2)
            print("\nFiles salvati nella cartella:", allfiles)
            
            # iterate on all files to move them to destination folder
            for file_path in allfiles:
                dst_path = os.path.join(percorso, os.path.basename(file_path))
                shutil.move(file_path, dst_path)
     
        print(f"{Fore.CYAN}{Style.BRIGHT}"+s7)  
        prompt= input("")
                
        
    
app()
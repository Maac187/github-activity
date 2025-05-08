import requests
import json
import argparse

def getUserActivity(userName):
        url=("https://api.github.com/users/"+userName+"/events")


def main():
       parser= argparse.ArgumentParser(description="user_activity_search")
       parser.add_argument("comando",help="obtener informacion con el username")
       parser.add_argument("username",help="mombre del usuario")

       arguments = parser.parse_args()
     
       if arguments.comando=="github-activity":
               getUserActivity(arguments.username)
       else:
               parser.print_help()
      



if __name__ == "__main__":
         main()
import cmd 

class MyCMD(cmd.Cmd):
    prompt = '$ '

    def do_help(self, arg):
        print(f"help: {arg}")

MyCMD().cmdloop()


#  def parse_command(self, inpt, args=None):
#         """parses a command by passing the input command to the relevant handler"""

#         cmd, args = self.clean_input(inpt)
    
#     # TODO come up with a way to show/hint aliases nicely
#         # empty command, return to prompt
#         if cmd == "":
#             pass 
    
#         elif cmd in ["help", "h"]:
#             self.show_help(cmd, args)

#         elif cmd in ["party", "p"]:
#             self.party()

#         elif cmd in ["tracks", "t"]:
#             self.tracks(args)

#         elif cmd in ["inventory", "i", "inv"]:
#             self.inventory(args)
        
#         elif cmd in ["fight"]:
#             self.fight()

#         elif cmd in ["exit", "quit"]:
#             self.safely_quit()

#         else:
#             self.console.print(f"[italic red]Command not recognized [/italic red]")

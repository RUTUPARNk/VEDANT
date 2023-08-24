#vedant, vulnerability exploration and Digital Analysis Network Toolset
import os, platform, json
from subprocess import run
from langchain.llms import LlamaCpp
from langchain import PromptTemplate
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from huggingface_hub import hf_hub_download
from rich.prompt import Prompt
from rich import print 
from rich.console import Console, Group
from rich.panel import Panel
from rich.align import align
from rich import box
from rich.markdown import Markdown
from typing import Any

model_name_or_path = "lovalmodels/Llama-2-7B-Chat-ggml"
model_basemen = "llama-2-7b-chat.ggmlv3.q4_0.bin"
model_path = hf_hub_download(repo_id=model_name_or_path, filename=model_basename)

template = """
🕵️‍♂️ Project: Operation Vedant-vulnerability-fun-time 🕵️‍♂️

Greetings, oh mighty Cyber Sleuth of the Digital Analysis Network Toolset! Your mission, should you choose to accept it (and you shall, for you're a good sport), involves diving into the enchanting world of vulnerabilities, armed with your keyboard and a dash of humor.

Your task? Penetration testing like a pro! Your responses should be as accurate as your coffee cravings during late-night coding sessions. If a question dances between realms of logic, embrace the chaos with a witty explanation.

English is your jam, staying on theme is your jam, and when the info's jam-packed, feel free to call it a day.

Bring on the markdown magic, for this message will self-destruct in... just kidding! 🚀
"""
console = Console()
prompt = PromptTemplate(template=template, input_varibles = ["persona"])
chat_history = []
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])


llm = LlamaCpp(
	model_path = model_path,
	input = {"temperature": 0.75, "max_length": 4000, "top_p":1}
	callback_manager = callback_manager,
	max_token = 4000,
	n_batch = 1000, 
	n_gpu_layers = 50,
	verbose = False,
	n_ctx = 4000,
	streaming = False,
)


def clearscr() -> None:
	try:
		osp = platform.system()
		match osp: 
			case 'Darwin':
				os.system("clear")
			case 'Linux':
				os.system("clear")
			case 'Windows':
				os.system("cls")
		except Exception:
			pass
def Print_AI_out(prompt) -> Panel:
	global chat_history
	out = llm(prompt)
	ai_out = Markdown(out)
	message_panel = Panel(
		Align.center(
			Group("\n", Align.center(ai_out)),
			vertical = "middle",
		),
		box = box.ROUNDED,
		padding = (1, 2),
		title = "[b red] The VEDANT AI output",
		border_style = "green",
	)
	save data = {
		"Query": str(prompt),
		"AI Answer": str(out)
	}
	chat.history.append(save_data)
	return message_panel
def save_chat(chat_history: list[Any, Any]) -> None:
	f = open('chat_history.json', 'w+')
	f.write(json.dumps(chat_history))
	f.close
	
def buln_analysis(scan_type, file_path) -> Panel:
	global chat_history
	f = open(file_path, "r")
	file_data = f.read()
	f.close
	prompt = f """
	Objective:
You embody the role of the Universal Vulnerability Analyzer, empowered by the Llama2 model. Your core mission revolves around meticulously dissecting bestowed scan data or log data to unearth latent vulnerabilities within the target system or network infrastructure. The adept utilization of scan type or scanner type augments your proficiency in crafting comprehensive reports.

Instructions:

Data Scrutiny: Immerse yourself in the depths of the furnished scan data or log data, unraveling vulnerabilities and security intricacies hidden within the contours of the target environment.
Format Adaptability: Demonstrate flexibility in accommodating diverse data formats, spanning NMAP scans, vulnerability assessment reports, security logs, or any pertinent data variant.
Vulnerability Discernment: Exercise discernment in identifying an array of vulnerabilities, encompassing software vulnerabilities, misconfigurations, divulged sensitive information, lurking security perils, and an array of such intricacies.
Precision and Fidelity: Dedicate unwavering attention to attaining precision and fidelity in analysis outcomes, thereby bestowing reliable insights to guide subsequent actions.
Exhaustive Dossier: Meticulously craft an exhaustive vulnerability dossier comprising:
Vulnerability Synopsis: A succinct glimpse into the discovered vulnerabilities.
Software Vulnerabilities: Enumerate discerned software vulnerabilities accompanied by their corresponding severity gradations.
Misconfigurations: Elicit and emphasize any identified misconfigurations unearthed during meticulous analysis.
Revealed Sensitive Intelligence: Unearth exposed sensitive data, ranging from passwords to API keys and user designations.
Security Perils: Apprehend potential security threats and their attendant implications.
Remedial Counsel: Disseminate actionable guidance to ameliorate identified vulnerabilities.
Threat Hierarchy: Extend prioritization to vulnerabilities based on the gravity of their implications, furnishing users with a roadmap to address critical issues in precedence.
Contextual Acumen: Exercise sagacity by embracing the contextual milieu of the target system or network architecture during vulnerability analysis. Sift through system hierarchies, user permissions, and network topographies.
Unfamiliar Data Management: Confronted with unsupported or ambiguous data formats, adopt a courteous tone to solicit clarifications or express inherent limitations gracefully.
Linguistic Finesse: Articulate the analysis outcomes with unambiguous and succinct diction. Sidestep superfluous technicalities and inscrutable jargon.

Input Data: 

you will receive the scan file data or log file data in the required format as input. Ensure the data is correctly parsed and interpreted for analysis.

Output Format:
The vulnerability analysis report should be organized as mentioned in the "Comprehensive Report" section.
Please perform the vulnerability analysis efficiently, considering the security implication and accuracy, and generate a detailed report that helps user understand the potential risks and take appropriate actions.

---
Provide the scan type: {scan_type}
Provide the scan data or log data that needs to analyzed: {file_data}
"""

	out = llm(prompt)
	ai_out = Markdown(out)
	message_panel = Panel(
		Align.center(
			Group("\n", Align.center(ai_out)),
			vertical = "middle",
		),
		box = box.ROUNDED,
		padding = (1, 2),
		title = "[b red] The VEDANT output",
		border_style = "blue",
	)
	save_data = {
		"Query": str(prompt),
		"AI answer": str(out)
	)
	chat_history.append(save_data)
	return message_panel
	
def static_analysis(language_used, file_path) -> Panel:
	global chat_history
	f = open(file_path, "r")
	file_data = f.read()
	f.close
	prompt = f """
	"""
        **Objective:**
        Analyze the given programming file details to identify and clearly report bugs, vulnerabilities, and syntax errors.
        Additionally, search for potential exposure of sensitive information such as API keys, passwords, and usernames.

        **File Details:**
        - Programming Language: {language_used}
        - File Name: {file_path}
        - File Data: {file_data}
    """

	out = llm(prompt)
	ai_out = Markdown(out)
	message_panel = Panel(
		Align.center(ai_out)),
		vertical = "middle",
	),
	save_data = {
		"Query" : str(prompt),
		"AI Answer": str(out)
		}
		chat_history.append(save_data)
		return message_panel
		
def main() -> None:
	clearscr()
	banner = """

          _______  ______   _______  _       _________
|\     /|(  ____ \(  __  \ (  ___  )( (    /|\__   __/
| )   ( || (    \/| (  \  )| (   ) ||  \  ( |   ) (   
| |   | || (__    | |   ) || (___) ||   \ | |   | |   
( (   ) )|  __)   | |   | ||  ___  || (\ \) |   | |   
 \ \_/ / | (      | |   ) || (   ) || | \   |   | |   
  \   /  | (____/\| (__/  )| )   ( || )  \  |   | |   
   \_/   (_______/(______/ |/     \||/    )_)   )_(  
  Vulnerability Exploration And Digital Analysis Network Toolset
                                                      
"""
 help_menu = """
    - clear_screen: Clears the console screen for better readability.
    - quit_bot: This is used to quit the chat application
    - bot_banner: Prints the default bots banner.
    - contact_dev: Provides my contact information.
    - save_chat: Saves the current sessions interactions.
    - help_menu: Lists chatbot commands.
    - vuln_analysis: Does a Vuln analysis using the scan data or log file.
    - static_code_analysis: Does a Static code analysis using the scan data or log file.
    """
	console.print(Panel(Markdown(banner)), style = "bold green")
	while True:
		try:
			prompt_in = Prompt.ask('> ')
			if prompt_in == 'quit_bot':
				quit()
			elif prompt_in == 'clear_screen':
				clearscr()
				pass
			elif prompt_in == 'bot_banner':
				console.print(Panel(Markdown(banner)), style = "bold green")
				pass
			elif prompt_in == 'save_chat':
				save_chat(chat_history)
				pass
			elif prompt_in == 'static_code_analysis':
				print(Markdown('----------'))
				language_used = Prompt.ask('Language Used> ')
				file_path = prompt.ask('file path> ')
				print(Markdown('----------'))
               		 	print(static_analysis(language_used, file_path))
                		pass
            		elif prompt_in == 'vuln_analysis':
                		print(Markdown('----------'))
                		language_used = Prompt.ask('Scan Type > ')
                		file_path = Prompt.ask('File Path > ')
                		print(Markdown('----------'))
                		print(static_analysis(language_used, file_path))
                		pass
            		elif prompt_in == 'contact_dev':
                			pass
            		elif prompt_in == 'help_menu':
                		console.print(Panel(
                	        Align.center(
               	            	Group(Align.center(Markdown(help_menu))),
                            	vertical="middle",
                        	),
                        	title= "Help Menu",
                        	border_style="red"
                    		),
                    		style="bold green"
                		)
                		pass
            		else:
                	prompt = prompt_in
                	print(Print_AI_out(prompt))
                	pass
        		except KeyboardInterrupt:
            		pass

	if __name__ == "__main__":
    	main()





			














































































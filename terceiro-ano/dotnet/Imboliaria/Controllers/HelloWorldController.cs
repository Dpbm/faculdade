using Microsoft.AspNetCore.Mvc;
using System.Text.Encodings.Web;

namespace Imboliaria.Controllers{
	public class HelloWorldController:Controller{
		//default action
		public string Index(){
			// localhost/HelloWorld
			return "helllo world!";
		}

		//especific action
		public string Welcome(int id, string nome, int idade){
			// localhost/HelloWorld/Welcome
			// you can pass the paramters using:
			// localhost/HelloWorld/Welcome/{id}?nome={nome}&idade={idade}
			return HtmlEncoder.Default.Encode($"Hello {nome} you have {idade} years old and your id is: {id}");
		}
	}

}

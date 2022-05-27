{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "OOP PYTHON",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyM3m1bI8SZ9mYiIyFfdL9O2",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/OCTAVIAKOMSKAIKRU/solid-octo-succotash/blob/main/OOP_PYTHON.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cnp5u4-NF6Si"
      },
      "outputs": [],
      "source": [
        "# Object Oriented Programming with pyhton\n",
        "\n",
        "# Concets we find in OOP :\n",
        "      # Abstraction\n",
        "      # Polymorphism\n",
        "      # Encapsulation\n",
        "      # Attributes and Objects\n",
        "      # Abstract classes\n",
        "      # Method kinds"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# To learn OOP we will be creating a function to learn from while adding certain complexities we need to know about the program"
      ],
      "metadata": {
        "id": "dtduHPUAG7wh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Basic Pyhton skills we should have basic knowledge of are :\n",
        "     # Variables\n",
        "     # If Statements\n",
        "     # Functions\n",
        "     # For Loops"
      ],
      "metadata": {
        "id": "gmNUyzuzHSYy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# We  will be learning it through mainy a type of \"STORE MANAGEMENT SYSTEM\" , that we will add certain instenses,methods etc. as we go along.\n",
        "\n"
      ],
      "metadata": {
        "id": "w_0iVPG-Hrvf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# How to assign attributes into instences (Datatype) \n",
        "\n",
        "class item:\n",
        "  def caculate_total_price(self ,x ,y):\n",
        "   return x * y\n",
        "\n",
        "\n",
        "item1 = item() #instence/datatype\n",
        "item1.name = \"chowder\" #str\n",
        "item1.price = 100000000 #int\n",
        "item1.quantity = 2 #int\n",
        "print(item1.caculate_total_price(item1.price , item1.quantity))\n",
        "\n",
        "item2 = item()\n",
        "item2.name = \"batman\"\n",
        "item2.price = 777\n",
        "item2.quantity = 2\n",
        "print(item2.caculate_total_price(item2.price , item2.quantity))\n",
        "\n",
        "# Now we are going to create mathods and add them to our instences inside our class,\n",
        "\n",
        "# We are going to be creating a method called \"caculate_total_price\", \n",
        "\n",
        "# Because it would be a very equivilant method for our instence.\n",
        "\n",
        "# Your methods should always concede parameters. E.g \n",
        "      \n",
        "    #TypeERROR: caculatetotalprice() takes 0 positional arguments but 1 was given. \n",
        "\n",
        "# When you finally in a workplace enviroment, never mess up common convensions** (self)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2p0wFjgAIqHP",
        "outputId": "17312e1a-0a3a-4fa0-a53f-e44da4905172"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "200000000\n",
            "1554\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# In OOP we are going to encounter certain problems that will need a unique method,\n",
        "\n",
        "# This unique methods are called \"Magic methods\"\n",
        "\n",
        "# The one we are going to be using first is the \"__init__\" method function,\n",
        "\n",
        "# It will allow us to successfully instanciate an instance instantly.\n",
        "\n",
        "# You should always construct your attributes under the method\n",
        "\n",
        "\n",
        "class item:\n",
        "  def __init__(self, name:str, price:float, quantity=0):\n",
        "   self.name = name\n",
        "   self.price = price\n",
        "   self.quantity = quantity\n",
        "  def caculate_total_price (self):\n",
        "    return self.price * self.quantity\n",
        "\n",
        "item1 = item(\"chowder\" ,100000000 ,2)\n",
        "\n",
        "item2 = item(\"batman\" ,777, 2)\n",
        "\n",
        "print(item1.name)\n",
        "print(item2.name)\n",
        "print(item1.price)\n",
        "print(item2.price)\n",
        "print(item1.quantity)\n",
        "print(item2.quantity)\n",
        "\n",
        "print(item1.caculate_total_price())\n",
        "print(item2.caculate_total_price())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qlhNo-jkTsBs",
        "outputId": "84ec8dc3-05cc-4e5b-8cb1-c8d497a23295"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "chowder\n",
            "batman\n",
            "100000000\n",
            "777\n",
            "2\n",
            "2\n",
            "200000000\n",
            "1554\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# You can assign attributes to instences individually\n",
        "\n",
        "# You can also add on the type ins (init function) by using colon.\n",
        "\n",
        "# Then if we want to expand our innit function we could use validation methods to assert out arguments arent against our expectence,\n",
        "\n",
        "# By using \"Assert statements\".\n",
        "\n",
        "# It is a statement keyword that uses the matches and evaluates them to your expectations.\n",
        "\n",
        "\n",
        "class Item :\n",
        "  def __init__(self ,name:str , price:float , quantity= 0):\n",
        "    #Running Validations\n",
        "    assert price >= 0, f\"Price {price} is nnot greater than or equal to 0\"\n",
        "    assert quantity >= 0, f\"Quantity {quantity} is not greater than or equal to 0\"\n",
        "\n",
        "    #Assigned Objects\n",
        "    self.name = name\n",
        "    self.price = price\n",
        "    self.quantity = quantity\n",
        "\n",
        "  def caculate_total_price(self):\n",
        "    return self.price * self.quantity\n",
        "\n",
        "Item1 = Item(\"chowder\" , 45.3 , 3)\n",
        "Item2 = Item(\"Batman\" , 2 , 2)\n",
        "\n",
        "print(Item1.caculate_total_price())\n",
        "print(Item2.caculate_total_price()) \n",
        "\n",
        "# So if your code were to run and give a number less than 0 , if will then give back an \"ASSERTION ERROR\""
      ],
      "metadata": {
        "id": "3IgBylHiZnkU",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0c3e12ef-9aa3-4b3a-ee62-220a88d2cad0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "135.89999999999998\n",
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        " # Then if you want to have access to certain elements in your instances or classes you could use a \"__dict__\" function.\n",
        "\n",
        " # This will allow you to access this instance or class by way of a dictionary python function.\n",
        "\n",
        "\n",
        " # In order for us to increase our learning capabilty we are going to construct a very formal and assertive class function.\n",
        "\n",
        " # We wiil have to assign a real life situation to our learning more time from now on.\n",
        "\n",
        " # E.g \n",
        "    # We had made a small online store back home that sold items at a small quantity and cheap price to the community to raise funds to buy certain things needed back home.\n",
        "    # We sell two different items shoes(ITEM1) and socks(ITEM2).\n",
        "    # The price for the shoes are R50 and R20 for every per socks.\n",
        "    # The quantity per month is 100 each.\n",
        "    # The only discount we have 25% of total price if you buy R60 worth of socks.\n",
        "\n",
        "\n",
        "class Item :\n",
        "  pay_rate = 0.45        # Pay_rate applied after the discount of 25%\n",
        "  def __init__(self,name: str, price: float , quantity= 0):\n",
        "    #Running Validations\n",
        "    assert price >= 0, f\"Price {price} is not greater or equal to 0\"\n",
        "    assert quantity >= 0, f\"Quantity {quantity} is not greater than or eaual to 0\"\n",
        "\n",
        "\n",
        "    #Assign objects\n",
        "    self.name = name\n",
        "    self.price = price\n",
        "    self.quantity = quantity\n",
        "\n",
        "  def caculate_total_price(self):\n",
        "    return self.price * self.quantity\n",
        "\n",
        "  def apply_discount(self):\n",
        "    self.price = self.price * self.pay_rate\n",
        "\n",
        "Item1 = Item(\"Shoes\" ,50 ,80)  # So for a particular month we sold 80 pers of shoes.\n",
        "print(Item1.caculate_total_price())\n",
        "\n",
        "Item2 = Item(\"Socks\" ,100 ,100) # ..and sold out on socks.\n",
        "Item2.pay_rate = 0.45\n",
        "Item2.apply_discount()\n",
        "print(Item2.price)\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QCwvsv5es8Np",
        "outputId": "551db18f-3c57-428b-8661-73131f2044aa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4000\n",
            "45.0\n"
          ]
        }
      ]
    }
  ]
}
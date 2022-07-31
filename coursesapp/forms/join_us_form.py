from django import forms
from coursesapp.models.joinus import JoinUs



class JoinUsForm(forms.ModelForm):
    class Meta:
        model = JoinUs
        fields = ['full_name', 'hsc_batch', 'department', 'your_aap_roll', 'currently_studying', 'your_free_time','contact', 'why_choose_us']

        labels = {
        "full_name" : "তোমার পুরো নাম?",
        "hsc_batch": "তোমার এইচএসসি ব্যাচ?",
        "department": "তুমি কোন ডিপার্টমেন্টে কাজ করতে আগ্রহী?",
        "your_aap_roll": "তোমার AAP-Roll?",
        "currently_studying" : "তোমার বর্তমান শিক্ষা প্রতিষ্ঠান?",
        "your_free_time": "দৈনিক তোমার কতটুক সময় ফ্রী থাকে?",
        "contact": "যোগাযোগ নাম্বার?(Ex-Mobile Number/Messenger/Telegram Link)",
        "why_choose_us" : "তুমি কেন পাঠশালার সাথে কাজ করতে চাও, কাজে তোমার দায়িত্বশীল মতামত জানাও?"

    }

    
    

    




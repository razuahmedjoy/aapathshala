from django.db import models


class JoinUs(models.Model):
    CHOICES = (
        ("শিক্ষার্থীদের প্রশ্নের উত্তর দেয়া", "শিক্ষার্থীদের প্রশ্নের উত্তর দেয়া"),
        ("বিষয়ভিত্তিক প্রশ্ন সলভ ও প্রশ্ন তৈরি করা", "বিষয়ভিত্তিক প্রশ্ন সলভ ও প্রশ্ন তৈরি করা"),
        ("ফেসবুক গ্রুপ পরিচালনা করা", "ফেসবুক গ্রুপ পরিচালনা করা"),
        ("ফেসবুক পেজ পরিচালনা করা", "ফেসবুক পেজ পরিচালনা করা"),
        ("প্রশ্ন টাইপ করা - টাইপিং এ দক্ষ", "প্রশ্ন টাইপ করা - টাইপিং এ দক্ষ"),
        ("পাঠশালার লেকচারার হিসাবে যুক্ত হওয়া", "পাঠশালার লেকচারার হিসাবে যুক্ত হওয়া"),
        ("বিষয়ভিত্তিক লেকচার কন্টেন্ট তৈরি করা", "বিষয়ভিত্তিক লেকচার কন্টেন্ট তৈরি করা"),
        ("নিজ ক্যাম্পাসের আপডেট তথ্য সংগ্রহ ও জানানো", "নিজ ক্যাম্পাসের আপডেট তথ্য সংগ্রহ ও জানানো"),
        ("গ্রাফিক ডিজাইনার – পোস্টার ডিজাইন করা", "গ্রাফিক ডিজাইনার – পোস্টার ডিজাইন করা"),
        ("পিডিএফ তৈরি করা – স্ক্যান করে", "পিডিএফ তৈরি করা – স্ক্যান করে")
        
    )

    HSC_CHOICES = (
        ("HSC-19", "HSC-19"),
        ("HSC-20", "HSC-20"),
        ("HSC-21", "HSC-21"),
        ("HSC-22", "HSC-22")

    )


    full_name = models.CharField(max_length=64)
    hsc_batch = models.CharField(max_length=64, choices=HSC_CHOICES)
    department = models.CharField(max_length=264, choices=CHOICES)
    your_aap_roll = models.CharField(max_length=64)
    currently_studying = models.CharField(max_length=264)
    your_free_time = models.CharField(max_length=64)
    contact = models.CharField(max_length=264)
    why_choose_us = models.TextField()

    class Meta:
        verbose_name_plural = "Join Us"
    
    def __str__(self):
        return self.full_name
        
import streamlit as st
import pandas as pd
import numpy as np
import joblib

def get_model():
    model = joblib.load("rf_model.pkl")
    return model

st.set_page_config(layout='wide')

st.header('MedTechCare')
tab_saglik, tab_hakkinda, tab_model = st.tabs(['Hastalıklar', 'Hakkımızda', 'Diyabetmisin?'])

col_diabet, col_kanser = tab_saglik.columns(2)

col_diabet.subheader('Diyabet Nedir?')

col_diabet.markdown('Diyabet, vücudunuzun kan şekeri seviyelerini düzenleme yeteneğini etkileyen bir metabolik bozukluktur. İki ana türü vardır: Tip 1 diyabet ve Tip 2 diyabet. ')
col_diabet.markdown('Tip 1 Diyabet: Bağışıklık sistemi, pankreastaki beta hücrelerine saldırarak insülin üretimini durdurur. Bu durum genellikle genetik yatkınlığa dayanır ve genç yaşlarda ortaya çıkar.')
col_diabet.markdown('Tip 2 Diyabet: Vücut, üretilen insüline uygun şekilde tepki vermez veya yeterince insülin üretmez. Genellikle yaşam tarzı faktörleri, obezite, genetik yatkınlık gibi nedenlerle ortaya çıkar.')
col_diabet.image('media/diyabet-seker-hastaligi.webp')
col_diabet.markdown('Diyabeti önlemek veya yönetmek için aşağıdaki adımları takip edebilirsiniz: Sağlıklı Beslenme: Dengeli ve düzenli bir diyet benimseyin. Şeker içeriği yüksek gıdalardan kaçının, lifli gıdalar tüketin ve porsiyonları kontrol altında tutun. Düzenli Egzersiz: Haftada en az 150 dakika orta düzeyde egzersiz yapın. Egzersiz, insülin direncini azaltabilir ve kan şekerini düzenlemeye yardımcı olabilir. Sağlıklı Kilo: Sağlıklı bir kiloyu korumak, tip 2 diyabet riskinizi azaltabilir. Gerektiğinde kilo vermek, kan şekerinizi kontrol altında tutmaya yardımcı olabilir. Stres Yönetimi: Stres, kan şekeri seviyelerini etkileyebilir. Stresle baş etme teknikleri öğrenmek ve düzenli olarak uygulamak önemlidir. Düzenli Kontroller: Düzenli olarak kan şekerinizi kontrol ettirin ve gerekirse doktorunuzun önerdiği testleri yaptırın. Sigara ve Alkol Kısıtlaması: Sigara içmek ve aşırı alkol tüketmek, diyabet riskinizi artırabilir. Bu maddelerden kaçınmak sağlığınızı iyileştirebilir. Genetik Riskinizi Değerlendirin: Ailede diyabet öyküsü varsa, bu durumu izlemek ve sağlık profesyoneli ile konuşmak önemlidir. Her bireyin sağlık durumu farklıdır, bu nedenle diyabet riskinizi belirlemek ve önlemler almak için bir sağlık uzmanına danışmanız önemlidir.')

col_kanser.subheader('Kanser Nedir?')
col_kanser.markdown('Kanser, vücut hücrelerinin kontrolsüz bir şekilde büyümesi ve çoğalması sonucu oluşan bir grup hastalığı ifade eder. Kanser hücreleri normal hücrelerin işlevini bozar ve vücutta hasara neden olabilir. Kanser genellikle organlarda veya dokularda başlar ve zamanla yayılabilir. Farklı kanser türleri farklı organlarda başlar.')
col_kanser.image('media/kanser.jpg')
col_kanser.markdown('Kanserin Nedenleri: Genetik Faktörler: Bazı kanser türleri genetik yatkınlığa bağlı olarak ortaya çıkabilir. Çevresel Etkenler: Sigara içmek, aşırı güneşe maruz kalmak, bazı kimyasallara maruz kalmak gibi çevresel faktörler kanser riskini artırabilir. İnflamasyon: Kronik inflamasyon, bazı kanser türlerinin oluşumunu teşvik edebilir. Virüsler ve Enfeksiyonlar: Human Papillomavirus (HPV), Hepatit B ve C, Human Immunodeficiency Virus (HIV) gibi virüsler kanser riskini artırabilir. Beslenme ve Yaşam Tarzı: Sağlıksız beslenme, obezite, düşük fiziksel aktivite seviyeleri kanser riskini artırabilir. Kanseri Önleme ve Risk Azaltma: Sigara ve Alkol Kısıtlaması: Sigara içmemek ve aşırı alkol tüketmemek kanser riskini azaltabilir. Sağlıklı Beslenme: Meyve, sebze, tam tahıllar ve düşük yağlı protein kaynakları içeren bir diyet, kanser riskini azaltabilir. Fiziksel Aktivite: Düzenli egzersiz yapmak, kanser riskini azaltabilir. Koruyucu Aşılar: HPV, hepatit B gibi virüslere karşı aşılar almak, ilgili kanser türlerine karşı koruma sağlayabilir. Düzenli Kontroller: Belirli kanser türleri için düzenli tarama testleri yaptırmak, erken tanı ve tedavi şansını artırabilir. UV Işınlardan Korunma: Güneşin zararlı UV ışınlarına karşı korunmak, deri kanseri riskini azaltabilir. Sağlıklı Kiloyu Koruma: Sağlıklı bir kiloda kalmak, kanser riskini azaltabilir. Stres Yönetimi: Stresle baş etmek için sağlıklı yöntemler kullanmak, genel sağlık durumunu iyileştirebilir. Çevresel Etkenlerden Kaçınma: Tehlikeli kimyasallardan kaçınmak ve işyerinde güvenlik önlemlerine uymak önemlidir. Kanserle mücadelede erken tanı büyük önem taşır. Belirtiler fark edildiğinde veya belirli yaş aralıklarında tarama testleri önerildiğinde doktora başvurmak önemlidir. Unutmayın ki herkesin kanser riski farklıdır, bu nedenle kişiselleştirilmiş bir sağlık planı oluşturmak için bir sağlık profesyoneli ile görüşmek önemlidir.')

col_string, col_image = tab_hakkinda.columns(2)
col_string.header('Hoş Geldiniz! MedTechCare')
col_string.markdown("MedTechCare, sağlık sektöründe teknoloji ve inovasyonu bir araya getirerek, bireylerin sağlık deneyimini dönüştürmeyi amaçlayan bir sağlık teknolojisi startup'ıdır. Sağlık hizmetlerini daha erişilebilir, kişisel ve etkili kılmak için en son teknolojiyi kullanarak, MedTechCare olarak sağlıklı bir gelecek inşa etmeye kararlıyız.")
col_string.markdown("Vizyonumuz MedTechCare olarak vizyonumuz, herkesin en kaliteli sağlık hizmetlerine ulaşabileceği bir dünya yaratmaktır. Teknolojinin gücünü kullanarak, sağlık hizmetlerini daha yakın, daha anlamlı ve daha etkili hale getirerek toplumumuzun sağlık standartlarını yükseltmeyi hedefliyoruz.")
col_string.markdown("Misyonumuz Misyonumuz, bireylerin sağlık yönetimini kolaylaştırmak ve sağlık profesyonellerine daha etkili araçlar sunmak üzerinedir. MedTechCare olarak, hasta odaklı çözümler geliştirmek, sağlık alanındaki en son gelişmeleri takip etmek ve inovasyonla sağlık sistemini dönüştürmek için çalışıyoruz.")

col_image.image('media/doktor_yapay_zeka-1.jpg')

# TAB MODEL

model = get_model()

pregnancies = tab_model.number_input('Hamilelik Sayınız: ', min_value=0, max_value=30, value=1)
glucose = tab_model.number_input('Glikoz değeriniz: ', min_value=20, max_value=300, value=100)
bloodpressure = tab_model.number_input('Tansiyon değeriniz: ', min_value=40, max_value=300, value=100)
skinthickness = tab_model.number_input('Cilt Kalınlığı değeriniz: ', min_value=0, max_value=500, value=40)
insulin = tab_model.number_input('İnsülin değeriniz: ', min_value=0, max_value=500, value=100)
bmi = tab_model.number_input('Vücut kitle indexisiniz: ', min_value=0, max_value=500, value=40)
diabetespedigreefunction = tab_model.number_input('Genetik diyabet riskiniz: ', min_value=0, max_value=10, value=2)
age = tab_model.number_input('Yaşınnızı giriniz: ', min_value=1, max_value=140, value=18)


X = [pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age]
if tab_model.button('Tahmin Et!'):
    prediction = model.predict(pd.DataFrame(X).T)
    if prediction == 1:
        tab_model.success(f'Diyabetsiniz çok geçmiş olsun.')
    else:
        tab_model.success(f'Diyabet değilsiniz sağlıklı günler dileriz.')
        st.balloons()













































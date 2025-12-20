"""
AI Sınav Sorusu Üretici - Ultra Modern Animasyonlu Versiyonu
Gerekli kurulum:
pip install customtkinter pillow
"""

import customtkinter as ctk
from tkinter import scrolledtext, messagebox, filedialog
from datetime import datetime
import threading
import os
import json
import time

# CustomTkinter ayarları
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AnimatedButton(ctk.CTkButton):
    """Gelişmiş animasyonlu buton"""
    def __init__(self, master, **kwargs):
        self.hover_color = kwargs.pop('hover_color_custom', None)
        self.default_color = kwargs.get('fg_color', "#3b82f6")
        super().__init__(master, **kwargs)
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)
        
    def on_hover(self, event):
        self.configure(cursor="hand2")
        if self.hover_color:
            self.after(0, lambda: self.configure(fg_color=self.hover_color))
        
    def on_leave(self, event):
        if self.hover_color:
            self.after(0, lambda: self.configure(fg_color=self.default_color))


class SinavSorusuUretici:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Sınav Sorusu Üretici - Demo Modu")
        self.root.geometry("1600x900")
        self.root.minsize(1400, 800)
        
        # Gradient arka plan
        self.root.configure(fg_color=("#f1f5f9", "#0f172a"))
        
        # Animasyon değişkenleri
        self.animation_running = False
        self.progress_value = 0
        
        # Veriler
        self.dersler = ["Matematik", "Fen Bilimleri", "Türkçe", "İngilizce", 
                        "Sosyal Bilgiler", "Fizik", "Kimya", "Biyoloji", "Tarih", "Coğrafya"]
        self.siniflar = ["5", "6", "7", "8", "9", "10", "11", "12"]
        self.zorluklar = ["Kolay", "Orta", "Zor"]
        self.soru_tipleri = {
            "Çoktan Seçmeli": "🔘",
            "Açık Uçlu": "📝",
            "Karışık": "🔀"
        }
        
        # İstatistikler
        self.toplam_uretilen = 0
        self.son_konu = ""
        self.mevcut_sorular = ""
        self.mevcut_cevaplar = ""
        
        # Kayıtlar klasörü
        if not os.path.exists("sorular"):
            os.makedirs("sorular")
        
        # Ayarlar dosyası
        self.ayarlar_dosyasi = "ayarlar.json"
        self.load_settings()
        
        self.create_modern_ui()
        
        # Başlangıç animasyonu
        self.root.after(100, self.start_welcome_animation)
    
    def load_settings(self):
        """Kayıtlı ayarları yükler"""
        try:
            if os.path.exists(self.ayarlar_dosyasi):
                with open(self.ayarlar_dosyasi, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.toplam_uretilen = data.get('toplam_uretilen', 0)
        except:
            pass
    
    def save_settings(self):
        """Ayarları kaydeder"""
        try:
            data = {
                'toplam_uretilen': self.toplam_uretilen,
                'son_guncelleme': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            with open(self.ayarlar_dosyasi, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except:
            pass
    
    def start_welcome_animation(self):
        """Hoş geldin animasyonu"""
        self.fade_in_element(self.status_label, 0, 1.0, 30)
    
    def fade_in_element(self, element, current_alpha, target_alpha, steps):
        """Element için fade-in animasyonu"""
        if current_alpha < target_alpha:
            current_alpha += (target_alpha / steps)
            # Alpha değerini renk ile simüle et
            try:
                element.configure(text_color=f"#{int(16*current_alpha):01x}{int(176*current_alpha):02x}{int(129*current_alpha):02x}")
            except:
                pass
            self.root.after(20, lambda: self.fade_in_element(element, current_alpha, target_alpha, steps))
    
    def animate_progress_bar(self, target_value, duration_ms=2000):
        """Progress bar animasyonu"""
        steps = 50
        step_duration = duration_ms // steps
        current = self.progress.get()
        increment = (target_value - current) / steps
        
        def update_step(current_value, step_count):
            if step_count < steps:
                new_value = current_value + increment
                self.progress.set(new_value)
                self.root.after(step_duration, lambda: update_step(new_value, step_count + 1))
            else:
                self.progress.set(target_value)
        
        update_step(current, 0)
    
    def pulse_button(self, button, count=0):
        """Buton için nabız animasyonu"""
        if count < 3:
            colors = [
                ("#dc2626", "#b91c1c"),
                ("#ef4444", "#dc2626"),
                ("#dc2626", "#b91c1c")
            ]
            color = colors[count % len(colors)]
            button.configure(fg_color=color[0])
            self.root.after(300, lambda: self.pulse_button(button, count + 1))
        else:
            button.configure(fg_color=("#dc2626", "#b91c1c"))
    
    def typing_effect(self, text_widget, text, index=0, delay=20):
        """Yazı yazma efekti"""
        if index < len(text):
            text_widget.insert("end", text[index])
            text_widget.see("end")
            self.root.after(delay, lambda: self.typing_effect(text_widget, text, index + 1, delay))
    
    def create_modern_ui(self):
        # Ana Container
        main_container = ctk.CTkFrame(self.root, fg_color="transparent")
        main_container.pack(fill="both", expand=True, padx=30, pady=30)
        
        # ============= MODERN HEADER =============
        header = ctk.CTkFrame(
            main_container,
            fg_color=("#ffffff", "#1e293b"),
            corner_radius=25,
            border_width=0
        )
        header.pack(fill="x", pady=(0, 25))
        
        # Header içerik
        header_content = ctk.CTkFrame(header, fg_color="transparent")
        header_content.pack(fill="both", padx=40, pady=30)
        
        # Logo + Başlık
        title_container = ctk.CTkFrame(header_content, fg_color="transparent")
        title_container.pack(side="left")
        
        # Büyük modern başlık
        title = ctk.CTkLabel(
            title_container,
            text="🎓  AI Sınav Sorusu Üretici",
            font=ctk.CTkFont(family="Segoe UI", size=38, weight="bold"),
            text_color=("#1a1a1a", "#f8fafc")
        )
        title.pack(anchor="w")
        
        subtitle = ctk.CTkLabel(
            title_container,
            text="Yapay Zeka Destekli • Müfredata Uygun • Demo Modu",
            font=ctk.CTkFont(family="Segoe UI", size=14),
            text_color=("#64748b", "#94a3b8")
        )
        subtitle.pack(anchor="w", pady=(8, 0))
        
        # Sağ taraf bilgi badge'leri
        badges_container = ctk.CTkFrame(header_content, fg_color="transparent")
        badges_container.pack(side="right")
        
        badge_data = [
            ("🤖", "Demo Modu", "#10b981"),
            ("✨", "AI Powered", "#8b5cf6"),
            ("📚", "5-12. Sınıf", "#f59e0b")
        ]
        
        for emoji, text, color in badge_data:
            badge = ctk.CTkFrame(
                badges_container,
                fg_color=color,
                corner_radius=18,
                height=45
            )
            badge.pack(side="top", pady=4)
            
            badge_label = ctk.CTkLabel(
                badge,
                text=f"{emoji} {text}",
                font=ctk.CTkFont(size=13, weight="bold"),
                text_color="#ffffff"
            )
            badge_label.pack(padx=20, pady=10)
        
        # ============= MAIN CONTENT AREA =============
        content_area = ctk.CTkFrame(main_container, fg_color="transparent")
        content_area.pack(fill="both", expand=True)
        content_area.grid_columnconfigure(1, weight=1)
        content_area.grid_rowconfigure(0, weight=1)
        
        # ============= SOL PANEL - MODERN CONTROL CENTER =============
        left_panel_container = ctk.CTkFrame(
            content_area,
            fg_color="transparent",
            width=450
        )
        left_panel_container.grid(row=0, column=0, sticky="nsew", padx=(0, 20))
        left_panel_container.pack_propagate(False)
        
        left_panel = ctk.CTkScrollableFrame(
            left_panel_container,
            fg_color=("#ffffff", "#1e293b"),
            corner_radius=25
        )
        left_panel.pack(fill="both", expand=True)
        
        # FORM SECTION
        form_section = ctk.CTkFrame(left_panel, fg_color="transparent")
        form_section.pack(fill="x", padx=25, pady=(25, 20))
        
        # Ders Seçimi
        self.create_form_field(form_section, "📚 Ders", 0)
        self.ders_var = ctk.StringVar(value=self.dersler[0])
        ders_menu = ctk.CTkOptionMenu(
            form_section,
            variable=self.ders_var,
            values=self.dersler,
            font=ctk.CTkFont(size=14),
            dropdown_font=ctk.CTkFont(size=13),
            height=45,
            corner_radius=12,
            fg_color=("#667eea", "#667eea"),
            button_color=("#764ba2", "#764ba2"),
            button_hover_color=("#6b46a1", "#6b46a1")
        )
        ders_menu.pack(fill="x", pady=(5, 15))
        
        # Sınıf Seçimi
        self.create_form_field(form_section, "🎯 Sınıf Seviyesi", 1)
        self.sinif_var = ctk.StringVar(value=self.siniflar[2])
        sinif_menu = ctk.CTkOptionMenu(
            form_section,
            variable=self.sinif_var,
            values=self.siniflar,
            font=ctk.CTkFont(size=14),
            dropdown_font=ctk.CTkFont(size=13),
            height=45,
            corner_radius=12,
            fg_color=("#667eea", "#667eea"),
            button_color=("#764ba2", "#764ba2"),
            button_hover_color=("#6b46a1", "#6b46a1")
        )
        sinif_menu.pack(fill="x", pady=(5, 15))
        
        # Konu Girişi
        self.create_form_field(form_section, "💡 Konu", 2)
        self.konu_entry = ctk.CTkEntry(
            form_section,
            placeholder_text="Örn: Oran Orantı, Fotosentez, Osmanlı İmparatorluğu",
            font=ctk.CTkFont(size=14),
            height=45,
            corner_radius=12,
            border_width=2
        )
        self.konu_entry.pack(fill="x", pady=(5, 15))
        
        # Soru Sayısı
        self.create_form_field(form_section, "🔢 Soru Sayısı", 3)
        self.soru_sayisi_var = ctk.IntVar(value=5)
        
        slider_container = ctk.CTkFrame(form_section, fg_color="transparent")
        slider_container.pack(fill="x", pady=(5, 15))
        
        self.soru_label = ctk.CTkLabel(
            slider_container,
            text="5",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=("#667eea", "#8b5cf6")
        )
        self.soru_label.pack(side="left", padx=(0, 15))
        
        soru_slider = ctk.CTkSlider(
            slider_container,
            from_=3,
            to=15,
            number_of_steps=12,
            variable=self.soru_sayisi_var,
            command=self.update_soru_label,
            height=20,
            button_length=25,
            fg_color=("#cbd5e1", "#475569"),
            progress_color=("#667eea", "#8b5cf6"),
            button_color=("#667eea", "#8b5cf6"),
            button_hover_color=("#764ba2", "#764ba2")
        )
        soru_slider.pack(side="left", fill="x", expand=True)
        
        # Zorluk Seviyesi Card
        zorluk_card = ctk.CTkFrame(
            left_panel,
            fg_color=("#f8fafc", "#0f172a"),
            corner_radius=20
        )
        zorluk_card.pack(fill="x", padx=25, pady=(0, 20))
        
        zorluk_inner = ctk.CTkFrame(zorluk_card, fg_color="transparent")
        zorluk_inner.pack(fill="x", padx=30, pady=25)
        
        ctk.CTkLabel(
            zorluk_inner,
            text="⚡ ZORLUK SEVİYESİ",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=("#94a3b8", "#64748b")
        ).pack(anchor="w", pady=(0, 15))
        
        self.zorluk_var = ctk.StringVar(value="Orta")
        
        zorluk_buttons = ctk.CTkFrame(zorluk_inner, fg_color="transparent")
        zorluk_buttons.pack(fill="x")
        
        zorluk_colors = {
            'Kolay': ("#10b981", "#059669"),
            'Orta': ("#f59e0b", "#d97706"),
            'Zor': ("#ef4444", "#dc2626")
        }
        
        for zorluk in self.zorluklar:
            btn = ctk.CTkRadioButton(
                zorluk_buttons,
                text=zorluk,
                variable=self.zorluk_var,
                value=zorluk,
                font=ctk.CTkFont(size=14, weight="bold"),
                fg_color=zorluk_colors[zorluk][0],
                hover_color=zorluk_colors[zorluk][1],
                border_width_checked=8,
                border_width_unchecked=3
            )
            btn.pack(anchor="w", pady=5)
        
        # Soru Tipi Card
        tip_card = ctk.CTkFrame(
            left_panel,
            fg_color=("#f8fafc", "#0f172a"),
            corner_radius=20
        )
        tip_card.pack(fill="x", padx=25, pady=(0, 20))
        
        tip_inner = ctk.CTkFrame(tip_card, fg_color="transparent")
        tip_inner.pack(fill="x", padx=30, pady=25)
        
        ctk.CTkLabel(
            tip_inner,
            text="📄 SORU TİPİ",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=("#94a3b8", "#64748b")
        ).pack(anchor="w", pady=(0, 15))
        
        self.soru_tipi_var = ctk.StringVar(value="Çoktan Seçmeli")
        
        for tip, emoji in self.soru_tipleri.items():
            btn = ctk.CTkRadioButton(
                tip_inner,
                text=f"{emoji} {tip}",
                variable=self.soru_tipi_var,
                value=tip,
                font=ctk.CTkFont(size=13, weight="bold"),
                fg_color=("#3b82f6", "#2563eb"),
                hover_color=("#1d4ed8", "#1e40af")
            )
            btn.pack(anchor="w", pady=5)
        
        # ÜRET BUTONU - Hero Button
        btn_container = ctk.CTkFrame(left_panel, fg_color="transparent")
        btn_container.pack(fill="x", padx=25, pady=(0, 20))
        
        self.uret_button = AnimatedButton(
            btn_container,
            text="🎯  DEMO SORU ÜRET",
            command=self.soru_uret_threaded,
            height=110,
            corner_radius=22,
            font=ctk.CTkFont(family="Segoe UI", size=26, weight="bold"),
            fg_color=("#dc2626", "#b91c1c"),
            hover_color_custom=("#ef4444", "#dc2626"),
            text_color="#ffffff"
        )
        self.uret_button.pack(fill="x")
        
        # Hızlı Eylemler
        quick_actions = ctk.CTkFrame(left_panel, fg_color="transparent")
        quick_actions.pack(fill="x", padx=25, pady=(0, 20))
        
        quick_btn_style = {
            "height": 45,
            "corner_radius": 12,
            "font": ctk.CTkFont(size=12, weight="bold")
        }
        
        self.yeni_btn = AnimatedButton(
            quick_actions,
            text="🔄 Yeni Soru Seti",
            command=self.yeni_soru_seti,
            fg_color=("#06b6d4", "#0891b2"),
            hover_color_custom=("#0e7490", "#06b6d4"),
            **quick_btn_style
        )
        self.yeni_btn.pack(fill="x", pady=2)
        
        self.ornek_yukle_btn = AnimatedButton(
            quick_actions,
            text="📁 Örnek Konular",
            command=self.ornek_yukle,
            fg_color=("#8b5cf6", "#7c3aed"),
            hover_color_custom=("#6d28d9", "#5b21b6"),
            **quick_btn_style
        )
        self.ornek_yukle_btn.pack(fill="x", pady=2)
        
        # Status Card
        status_card = ctk.CTkFrame(
            left_panel,
            fg_color=("#f8fafc", "#0f172a"),
            corner_radius=20
        )
        status_card.pack(fill="x", padx=25, pady=(0, 20))
        
        status_inner = ctk.CTkFrame(status_card, fg_color="transparent")
        status_inner.pack(fill="x", padx=30, pady=25)
        
        ctk.CTkLabel(
            status_inner,
            text="DURUM",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=("#94a3b8", "#64748b")
        ).pack(anchor="w")
        
        self.status_label = ctk.CTkLabel(
            status_inner,
            text="● Hazır",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#10b981"
        )
        self.status_label.pack(anchor="w", pady=(12, 0))
        
        # İstatistik
        self.stat_label = ctk.CTkLabel(
            status_inner,
            text=f"📊 Toplam Üretilen: {self.toplam_uretilen}",
            font=ctk.CTkFont(size=12),
            text_color=("#64748b", "#94a3b8")
        )
        self.stat_label.pack(anchor="w", pady=(10, 0))
        
        # Progress Bar
        self.progress = ctk.CTkProgressBar(
            status_inner,
            height=8,
            corner_radius=4,
            fg_color=("#e2e8f0", "#334155"),
            progress_color=("#10b981", "#059669")
        )
        self.progress.pack(fill="x", pady=(15, 0))
        self.progress.set(0)
        
        # Features Card
        features_card = ctk.CTkFrame(
            left_panel,
            fg_color=("#f8fafc", "#0f172a"),
            corner_radius=20
        )
        features_card.pack(fill="x", padx=25, pady=(0, 25))
        
        features_inner = ctk.CTkFrame(features_card, fg_color="transparent")
        features_inner.pack(fill="x", padx=30, pady=25)
        
        ctk.CTkLabel(
            features_inner,
            text="ÖZELLİKLER",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=("#94a3b8", "#64748b")
        ).pack(anchor="w", pady=(0, 15))
        
        features = [
            ("🎯", "Akıllı Üretim", "Demo soru örnekleri"),
            ("📚", "Müfredata Uygun", "Türk eğitim sistemine özel"),
            ("⚡", "Hızlı Sonuç", "Anında hazır"),
            ("💾", "Otomatik Kayıt", "TXT formatında export")
        ]
        
        for emoji, title, desc in features:
            feature_item = ctk.CTkFrame(
                features_inner,
                fg_color=("#ffffff", "#0a0e1a"),
                corner_radius=12,
                border_width=1,
                border_color=("#e2e8f0", "#1e293b")
            )
            feature_item.pack(fill="x", pady=5)
            
            item_content = ctk.CTkFrame(feature_item, fg_color="transparent")
            item_content.pack(fill="x", padx=15, pady=12)
            
            ctk.CTkLabel(
                item_content,
                text=emoji,
                font=ctk.CTkFont(size=20)
            ).pack(side="left", padx=(0, 10))
            
            text_container = ctk.CTkFrame(item_content, fg_color="transparent")
            text_container.pack(side="left", fill="x", expand=True)
            
            ctk.CTkLabel(
                text_container,
                text=title,
                font=ctk.CTkFont(size=13, weight="bold"),
                anchor="w"
            ).pack(anchor="w")
            
            ctk.CTkLabel(
                text_container,
                text=desc,
                font=ctk.CTkFont(size=10),
                text_color=("#64748b", "#94a3b8"),
                anchor="w"
            ).pack(anchor="w")
        
        # ============= SAĞ PANEL - OUTPUT AREA =============
        right_panel = ctk.CTkFrame(
            content_area,
            fg_color=("#ffffff", "#1e293b"),
            corner_radius=25
        )
        right_panel.grid(row=0, column=1, sticky="nsew")
        
        # Tabview
        self.tabview = ctk.CTkTabview(
            right_panel,
            corner_radius=20,
            fg_color="transparent"
        )
        self.tabview.pack(fill="both", expand=True, padx=20, pady=20)
        
        # TAM METİN SEKMESI
        self.tabview.add("📝 SORULAR")
        text_tab = self.tabview.tab("📝 SORULAR")
        
        # Toolbar
        toolbar = ctk.CTkFrame(text_tab, fg_color="transparent")
        toolbar.pack(fill="x", pady=(0, 10))
        
        self.kaydet_btn = AnimatedButton(
            toolbar,
            text="💾 Kaydet",
            command=self.sorulari_kaydet,
            height=40,
            width=120,
            corner_radius=12,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=("#10b981", "#059669"),
            hover_color_custom=("#047857", "#065f46"),
            state="disabled"
        )
        self.kaydet_btn.pack(side="left", padx=(0, 5))
        
        self.kopyala_btn = AnimatedButton(
            toolbar,
            text="📋 Kopyala",
            command=self.sorulari_kopyala,
            height=40,
            width=120,
            corner_radius=12,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=("#3b82f6", "#2563eb"),
            hover_color_custom=("#1d4ed8", "#1e40af"),
            state="disabled"
        )
        self.kopyala_btn.pack(side="left", padx=5)
        
        self.yazdir_btn = AnimatedButton(
            toolbar,
            text="🖨️ Yazdır",
            command=self.sorulari_yazdir,
            height=40,
            width=120,
            corner_radius=12,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=("#8b5cf6", "#7c3aed"),
            hover_color_custom=("#6d28d9", "#5b21b6"),
            state="disabled"
        )
        self.yazdir_btn.pack(side="left", padx=5)
        
        self.temizle_btn = AnimatedButton(
            toolbar,
            text="🗑️ Temizle",
            command=self.sorulari_temizle,
            height=40,
            width=120,
            corner_radius=12,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=("#ef4444", "#dc2626"),
            hover_color_custom=("#b91c1c", "#991b1b"),
            state="disabled"
        )
        self.temizle_btn.pack(side="left", padx=5)
        
        # Text Output
        text_container = ctk.CTkFrame(
            text_tab,
            fg_color=("#f8fafc", "#0a0e1a"),
            corner_radius=15
        )
        text_container.pack(fill="both", expand=True)
        
        self.text_output = scrolledtext.ScrolledText(
            text_container,
            font=("Segoe UI", 13),
            wrap="word",
            bg="#0a0e1a",
            fg="#e2e8f0",
            insertbackground="#3b82f6",
            selectbackground="#3b82f6",
            selectforeground="#ffffff",
            borderwidth=0,
            padx=30,
            pady=30,
            relief="flat",
            spacing1=5,
            spacing2=3,
            spacing3=5
        )
        self.text_output.pack(fill="both", expand=True)
        
        # CEVAP ANAHTARI SEKMESI
        self.tabview.add("✅ CEVAPLAR")
        answer_tab = self.tabview.tab("✅ CEVAPLAR")
        
        answer_container = ctk.CTkFrame(
            answer_tab,
            fg_color=("#ecfdf5", "#0a0e1a"),
            corner_radius=15
        )
        answer_container.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.answer_output = scrolledtext.ScrolledText(
            answer_container,
            font=("Segoe UI", 13),
            wrap="word",
            bg="#0a0e1a",
            fg="#10b981",
            insertbackground="#10b981",
            selectbackground="#10b981",
            selectforeground="#000000",
            borderwidth=0,
            padx=30,
            pady=30,
            relief="flat",
            spacing1=5,
            spacing2=3,
            spacing3=5
        )
        self.answer_output.pack(fill="both", expand=True)
        
        # İSTATİSTİK SEKMESI
        self.tabview.add("📊 İSTATİSTİK")
        stat_tab = self.tabview.tab("📊 İSTATİSTİK")
        
        stat_frame = ctk.CTkScrollableFrame(
            stat_tab,
            fg_color="transparent"
        )
        stat_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # İstatistik kartları
        self.stat_card_toplam = self.create_stat_card(stat_frame, "Toplam Üretilen", str(self.toplam_uretilen), "🎯", "#10b981")
        self.stat_card_konu = self.create_stat_card(stat_frame, "Son Konu", self.son_konu or "Henüz yok", "📚", "#3b82f6")
        self.create_stat_card(stat_frame, "Mod", "Demo Sürüm", "⭐", "#f59e0b")
        self.create_stat_card(stat_frame, "Durum", "Aktif", "🔢", "#8b5cf6")
        
        # Başlangıç metinleri
        welcome_text = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       🎓  DEMO MODU - SORU ÜRETMEYE HAZIR!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨  NASIL ÇALIŞIR:
   • Sol taraftaki formu doldurun
   • Ders, sınıf ve konu seçin
   • 'DEMO SORU ÜRET' butonuna tıklayın

🚀  NE OLACAK:
   • Sistem demo sorular oluşturacak
   • Çoktan seçmeli veya açık uçlu örnekler
   • Cevap anahtarı otomatik gösterilecek
   • Dosya olarak kaydedebilirsiniz

⚠️  DİKKAT: Bu demo modudur!
📚  Gerçek AI entegrasyonu için API key gerekir
⚡  Şimdilik örnek sorular gösterilir

💡  TÜRKÇE KARAKTER DESTEĞİ:
   • ş, ğ, ü, ö, ç, ı karakterleri desteklenir
   • Osmanlı, İngilizce, Türkçe vb. yazabilirsiniz
"""
        
        answer_welcome = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              ✅  CEVAP ANAHTARI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊  CEVAPLAR BURADA GÖRÜNECEK

✨  OTOMATIK CEVAP ANAHTARI:
   • Doğru cevaplar işaretlenecek
   • Açıklamalar eklenecek
   • Puanlama önerileri sunulacak

🤖  Demo modunda örnek cevaplar!
"""
        
        self.text_output.insert("1.0", welcome_text)
        self.answer_output.insert("1.0", answer_welcome)
    
    def create_stat_card(self, parent, title, value, emoji, color):
        """İstatistik kartı oluşturur"""
        card = ctk.CTkFrame(
            parent,
            fg_color=("#ffffff", "#1e293b"),
            corner_radius=15,
            border_width=2,
            border_color=(color, color)
        )
        card.pack(fill="x", pady=10)
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill="x", padx=25, pady=20)
        
        # Emoji
        ctk.CTkLabel(
            content,
            text=emoji,
            font=ctk.CTkFont(size=40)
        ).pack(side="left", padx=(0, 20))
        
        # Text container
        text_cont = ctk.CTkFrame(content, fg_color="transparent")
        text_cont.pack(side="left", fill="x", expand=True)
        
        ctk.CTkLabel(
            text_cont,
            text=title,
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=("#64748b", "#94a3b8"),
            anchor="w"
        ).pack(anchor="w")
        
        value_label = ctk.CTkLabel(
            text_cont,
            text=value,
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=color,
            anchor="w"
        )
        value_label.pack(anchor="w")
        
        return card
    
    def create_form_field(self, parent, label_text, row):
        """Form alanı etiketi oluşturur"""
        ctk.CTkLabel(
            parent,
            text=label_text,
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=("#1e293b", "#f1f5f9"),
            anchor="w"
        ).pack(anchor="w")
    
    def update_soru_label(self, value):
        """Soru sayısı label'ını günceller"""
        self.soru_label.configure(text=str(int(value)))
    
    def soru_uret_threaded(self):
        """Thread ile soru üretir"""
        thread = threading.Thread(target=self.soru_uret, daemon=True)
        thread.start()
    
    def soru_uret(self):
        """Demo soru üretir"""
        konu = self.konu_entry.get().strip()
        
        if not konu:
            self.root.after(0, lambda: messagebox.showerror(
                "⚠️ Hata",
                "Lütfen bir konu giriniz!"
            ))
            return
        
        # UI güncelle
        self.root.after(0, self.uretim_basladi)
        
        # Parametreler
        ders = self.ders_var.get()
        sinif = self.sinif_var.get()
        soru_sayisi = int(self.soru_sayisi_var.get())
        zorluk = self.zorluk_var.get()
        soru_tipi = self.soru_tipi_var.get()
        
        try:
            # Demo bekleme efekti
            time.sleep(2)
            
            # Demo sorular üret
            sorular = self.generate_demo_questions(ders, sinif, konu, soru_sayisi, zorluk, soru_tipi)
            
            self.toplam_uretilen += 1
            self.son_konu = konu
            self.save_settings()
            
            self.root.after(0, lambda: self.sorulari_goster(sorular, ders, sinif, konu, zorluk, soru_tipi))
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror(
                "❌ Hata",
                f"Soru üretilirken hata oluştu:\n\n{str(e)}"
            ))
        
        finally:
            self.root.after(0, self.uretim_tamamlandi)
    
    def generate_demo_questions(self, ders, sinif, konu, soru_sayisi, zorluk, soru_tipi):
        """Demo sorular üretir"""
        sorular = []
        
        if soru_tipi == "Çoktan Seçmeli" or soru_tipi == "Karışık":
            for i in range(1, min(soru_sayisi + 1, 6)):
                soru = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SORU {i}:
{sinif}. sınıf {ders} dersinde "{konu}" konusuna ait örnek soru.
Zorluk seviyesi: {zorluk}

[Bu demo modda örnek bir sorudur. Gerçek AI entegrasyonu ile
otomatik olarak konuya özel sorular üretilecektir.]

A) Örnek şık A
B) Örnek şık B
C) Örnek şık C (Doğru Cevap)
D) Örnek şık D

✓ CEVAP: C - Bu demo için örnek cevaptır. Gerçek entegrasyonda
detaylı açıklamalar olacaktır.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
                sorular.append(soru)
        
        if soru_tipi == "Açık Uçlu":
            for i in range(1, min(soru_sayisi + 1, 4)):
                soru = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SORU {i}:
{sinif}. sınıf {ders} dersinde "{konu}" konusunu açıklayınız.
Zorluk seviyesi: {zorluk}

[Bu demo modda örnek bir açık uçlu sorudur.]

📝 CEVAP ANAHTARI:
Bu konu hakkında öğrencilerin bilmesi gerekenler:
- Ana kavramlar
- İlişkiler ve bağlantılar
- Örnekler

📊 PUANLAMA:
- Tam cevap: 10 puan
- Kısmi cevap: 5-7 puan
- Eksik cevap: 0-4 puan
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
                sorular.append(soru)
        
        return "\n".join(sorular)
    
    def uretim_basladi(self):
        """Üretim başladığında UI güncellenir"""
        self.animation_running = True
        
        # Buton animasyonu
        self.uret_button.configure(
            text="⏳  İŞLENİYOR...",
            state="disabled",
            fg_color=("#94a3b8", "#64748b")
        )
        
        # Status animasyonu
        self.status_label.configure(
            text="● Üretiliyor...",
            text_color="#f59e0b"
        )
        
        # Progress bar animasyonu
        self.animate_progress_bar(0.7, 2000)
        
        # Diğer butonları devre dışı bırak
        self.kaydet_btn.configure(state="disabled")
        self.kopyala_btn.configure(state="disabled")
        self.yazdir_btn.configure(state="disabled")
        self.temizle_btn.configure(state="disabled")
        
        # Typing effect
        self.text_output.delete("1.0", "end")
        loading_text = """
╔══════════════════════════════════════════════════════════╗
║                  🤖 AI ÇALlŞIYOR                         ║
╚══════════════════════════════════════════════════════════╝

✨ Demo sorular hazırlanıyor...
⚙️  Parametreler işleniyor...
🎯 Konu analiz ediliyor...
📝 Sorular oluşturuluyor...

Lütfen bekleyin...
"""
        self.typing_effect(self.text_output, loading_text, 0, 10)
    
    def uretim_tamamlandi(self):
        """Üretim tamamlandığında UI güncellenir"""
        self.animation_running = False
        
        # Buton animasyonu
        self.uret_button.configure(
            text="🎯  DEMO SORU ÜRET",
            state="normal",
            fg_color=("#dc2626", "#b91c1c")
        )
        
        # Status animasyonu
        self.status_label.configure(
            text="● Tamamlandı ✓",
            text_color="#10b981"
        )
        
        # Progress bar tamamla
        self.animate_progress_bar(1.0, 500)
        
        # İstatistik güncelle
        self.stat_label.configure(
            text=f"📊 Toplam Üretilen: {self.toplam_uretilen}"
        )
        
        # Pulse efekti
        self.pulse_button(self.status_label)
    
    def sorulari_goster(self, sorular, ders, sinif, konu, zorluk, soru_tipi):
        """Üretilen soruları gösterir"""
        # Metni temizle
        self.text_output.delete("1.0", "end")
        self.answer_output.delete("1.0", "end")
        
        # Header bilgisi
        header = f"""
╔══════════════════════════════════════════════════════════╗
║                    DEMO SORU KAĞIDI                       ║
╚══════════════════════════════════════════════════════════╝

📚 Ders: {ders}
🎯 Sınıf: {sinif}
💡 Konu: {konu}
⚡ Zorluk: {zorluk}
📄 Tip: {soru_tipi}
📅 Tarih: {datetime.now().strftime("%d.%m.%Y %H:%M")}
⚠️  MOD: DEMO - Örnek Sorular

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        
        # Soruları göster - typing effect ile
        full_text = header + sorular
        self.typing_effect(self.text_output, full_text, 0, 5)
        
        # Cevapları ayıkla ve göster
        cevap_metni = self.cevaplari_ayikla(sorular)
        
        answer_header = f"""
╔══════════════════════════════════════════════════════════╗
║                   CEVAP ANAHTARI                          ║
╚══════════════════════════════════════════════════════════╝

📚 Ders: {ders} | 🎯 Sınıf: {sinif}
💡 Konu: {konu}
📅 {datetime.now().strftime("%d.%m.%Y %H:%M")}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{cevap_metni}
"""
        
        self.answer_output.insert("1.0", answer_header)
        
        # Mevcut soruları sakla
        self.mevcut_sorular = full_text
        self.mevcut_cevaplar = cevap_metni
        
        # Butonları aktif et
        self.kaydet_btn.configure(state="normal")
        self.kopyala_btn.configure(state="normal")
        self.yazdir_btn.configure(state="normal")
        self.temizle_btn.configure(state="normal")
        
        # Başarı mesajı - animasyonlu
        self.root.after(500, lambda: messagebox.showinfo(
            "✅ Başarılı",
            f"✨ {self.soru_sayisi_var.get()} adet demo soru başarıyla oluşturuldu!\n\n"
            f"📝 Sorular ve cevap anahtarı hazır.\n"
            f"💾 Kaydet butonuyla dosyaya kaydedebilirsiniz.\n\n"
            f"⚠️  Bu demo modudur. Gerçek AI entegrasyonu için\n"
            f"Anthropic API key gereklidir."
        ))
    
    def cevaplari_ayikla(self, metin):
        """Sorulardan cevapları ayıklar"""
        cevaplar = []
        satirlar = metin.split('\n')
        
        for satir in satirlar:
            if '✓ CEVAP:' in satir or '📝 CEVAP ANAHTARI:' in satir or '📊 PUANLAMA:' in satir:
                cevaplar.append(satir)
        
        if cevaplar:
            return '\n'.join(cevaplar)
        else:
            return "Cevap anahtarı metin içinde yer almaktadır."
    
    def sorulari_kaydet(self):
        """Soruları dosyaya kaydeder"""
        if not self.mevcut_sorular:
            messagebox.showwarning("⚠️ Uyarı", "Kaydedilecek soru bulunamadı!")
            return
        
        # Dosya adı oluştur
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        konu_safe = self.konu_entry.get().strip().replace(" ", "_")[:30]
        dosya_adi = f"sorular/{self.ders_var.get()}_{self.sinif_var.get()}sinif_{konu_safe}_{timestamp}.txt"
        
        try:
            with open(dosya_adi, 'w', encoding='utf-8') as f:
                f.write(self.mevcut_sorular)
                f.write("\n\n" + "="*60 + "\n")
                f.write("CEVAP ANAHTARI\n")
                f.write("="*60 + "\n\n")
                f.write(self.mevcut_cevaplar)
            
            # Animasyonlu başarı mesajı
            self.pulse_button(self.kaydet_btn)
            
            messagebox.showinfo(
                "💾 Kaydedildi",
                f"✅ Sorular başarıyla kaydedildi!\n\n📁 {dosya_adi}\n\n"
                f"Dosya UTF-8 encoding ile kaydedildi.\n"
                f"Türkçe karakterler desteklenir."
            )
        except Exception as e:
            messagebox.showerror("❌ Hata", f"Kayıt hatası:\n{str(e)}")
    
    def sorulari_kopyala(self):
        """Soruları panoya kopyalar"""
        if not self.mevcut_sorular:
            messagebox.showwarning("⚠️ Uyarı", "Kopyalanacak soru bulunamadı!")
            return
        
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.mevcut_sorular)
            
            # Animasyon
            self.pulse_button(self.kopyala_btn)
            
            messagebox.showinfo(
                "📋 Kopyalandı", 
                "✅ Sorular panoya kopyalandı!\n\nİstediğiniz yere yapıştırabilirsiniz."
            )
        except Exception as e:
            messagebox.showerror("❌ Hata", f"Kopyalama hatası:\n{str(e)}")
    
    def sorulari_yazdir(self):
        """Soruları yazdırma için hazırlar"""
        if not self.mevcut_sorular:
            messagebox.showwarning("⚠️ Uyarı", "Yazdırılacak soru bulunamadı!")
            return
        
        # Geçici dosya oluştur
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        temp_file = f"sorular/yazdir_{timestamp}.txt"
        
        try:
            with open(temp_file, 'w', encoding='utf-8') as f:
                f.write(self.mevcut_sorular)
            
            # Animasyon
            self.pulse_button(self.yazdir_btn)
            
            messagebox.showinfo(
                "🖨️ Yazdırma",
                f"✅ Dosya oluşturuldu:\n📁 {temp_file}\n\n"
                "Bu dosyayı yazıcınızdan yazdırabilirsiniz.\n"
                "UTF-8 kodlamalı - Türkçe karakterler korunur."
            )
            
            # Dosyayı aç
            try:
                os.startfile(temp_file)
            except:
                pass
        except Exception as e:
            messagebox.showerror("❌ Hata", f"Yazdırma hatası:\n{str(e)}")
    
    def sorulari_temizle(self):
        """Soru çıktılarını temizler"""
        cevap = messagebox.askyesno(
            "🗑️ Temizle",
            "❓ Tüm soruları ve cevapları temizlemek istediğinize emin misiniz?\n\n"
            "Bu işlem geri alınamaz!"
        )
        
        if cevap:
            # Fade out animasyonu simülasyonu
            self.text_output.delete("1.0", "end")
            self.answer_output.delete("1.0", "end")
            
            welcome_text = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       ✅ TEMİZLENDİ - YENİ SORU ÜRETEBİLİRSİNİZ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Sol taraftaki formu doldurun
🚀 'DEMO SORU ÜRET' butonuna tıklayın
✨ Yeni sorular oluşturun!

💡 Türkçe karakter desteği aktif
📚 Demo mod çalışıyor
"""
            
            self.text_output.insert("1.0", welcome_text)
            self.answer_output.insert("1.0", "✅ CEVAP ANAHTARI\n\nTemizlendi. Yeni sorular üretebilirsiniz!")
            
            self.mevcut_sorular = ""
            self.mevcut_cevaplar = ""
            
            # Butonları devre dışı bırak
            self.kaydet_btn.configure(state="disabled")
            self.kopyala_btn.configure(state="disabled")
            self.yazdir_btn.configure(state="disabled")
            self.temizle_btn.configure(state="disabled")
            
            # Progress bar sıfırla
            self.animate_progress_bar(0, 500)
            
            # Status güncelle
            self.status_label.configure(
                text="● Hazır",
                text_color="#10b981"
            )
    
    def yeni_soru_seti(self):
        """Yeni soru seti için formu sıfırlar"""
        # Animasyonlu temizleme
        self.konu_entry.delete(0, "end")
        self.soru_sayisi_var.set(5)
        self.soru_label.configure(text="5")
        self.animate_progress_bar(0, 500)
        
        # Pulse animasyonu
        self.pulse_button(self.yeni_btn)
        
        messagebox.showinfo(
            "🔄 Yeni Set", 
            "✅ Form sıfırlandı!\n\n"
            "Yeni sorular üretebilirsiniz.\n"
            "💡 Farklı bir konu deneyin!"
        )
    
    def ornek_yukle(self):
        """Örnek konuları yükler"""
        ornekler = {
            "Matematik": [
                "Oran Orantı Problemleri",
                "Üslü Sayılar ve Köklü Sayılar", 
                "Cebirsel İfadeler ve Özdeşlikler",
                "Denklem Çözme Yöntemleri"
            ],
            "Fen Bilimleri": [
                "Fotosentez ve Solunum",
                "Elektrik Akımı ve Devreleri",
                "Kuvvet ve Hareket",
                "Maddenin Halleri"
            ],
            "Türkçe": [
                "Sözcük Türleri ve Görevleri",
                "Noktalama İşaretleri",
                "Anlatım Biçimleri ve Türleri",
                "Cümle Çeşitleri"
            ],
            "İngilizce": [
                "Present Continuous Tense",
                "Past Simple Tense",
                "Adjectives and Adverbs",
                "Modal Verbs"
            ],
            "Sosyal Bilgiler": [
                "Osmanlı İmparatorluğu'nun Kuruluşu",
                "Atatürk İlkeleri",
                "Türkiye'nin Coğrafi Bölgeleri",
                "Demokrasi ve İnsan Hakları"
            ],
            "Tarih": [
                "Osmanlı Devleti'nin Yükselişi",
                "Türk İnkılap Tarihi",
                "Kurtuluş Savaşı",
                "Atatürk Dönemi Reformları"
            ]
        }
        
        ders = self.ders_var.get()
        
        # Animasyon
        self.pulse_button(self.ornek_yukle_btn)
        
        if ders in ornekler:
            secenekler = ornekler[ders]
            mesaj = f"📚 {ders} için Örnek Konular:\n\n"
            mesaj += "\n".join([f"  • {k}" for k in secenekler])
            mesaj += "\n\n💡 İstediğiniz konuyu kopyalayıp yapıştırabilirsiniz!"
            messagebox.showinfo("📁 Örnek Konular", mesaj)
        else:
            messagebox.showinfo(
                "📁 Örnekler", 
                f"⚠️ {ders} dersi için örnek konu henüz eklenmedi.\n\n"
                "Kendi konunuzu yazabilirsiniz!"
            )


def main():
    """Ana program"""
    root = ctk.CTk()
    app = SinavSorusuUretici(root)
    
    # Pencere kapatma animasyonu
    def on_closing():
        if messagebox.askokcancel("Çıkış", "Programdan çıkmak istediğinize emin misiniz?"):
            root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()

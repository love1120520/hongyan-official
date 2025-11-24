# WAI-ARIA 使用指南

## 什麼是 WAI-ARIA？

WAI-ARIA（Web Accessibility Initiative - Accessible Rich Internet Applications）是 W3C 的 Protocols and Formats Working Group (PFWG) 的主要成果，用於提高網頁應用程式的可訪問性。

## 在網頁開發中使用 WAI-ARIA 的步驟

### 1. 了解 ARIA 的核心概念

ARIA 主要包含三個關鍵部分：
- **Roles（角色）**：定義元素的類型或用途
- **Properties（屬性）**：描述元素的特性
- **States（狀態）**：描述元素的當前狀態

### 2. 使用 ARIA Landmark Roles

Landmark roles 幫助屏幕閱讀器用戶快速導航頁面：

```html
<header role="banner">
  <h1>網站標題</h1>
</header>

<nav role="navigation">
  <ul>導航菜單</ul>
</nav>

<main role="main">
  <article>主要內容</article>
</main>

<aside role="complementary">
  側邊欄內容
</aside>

<footer role="contentinfo">
  版權信息
</footer>
```

### 3. 添加 ARIA 標籤

使用 `aria-label` 和 `aria-labelledby` 為元素提供可訪問的名稱：

```html
<!-- aria-label 直接提供標籤 -->
<button aria-label="關閉對話框">×</button>

<!-- aria-labelledby 引用其他元素的 ID -->
<section aria-labelledby="contact-heading">
  <h2 id="contact-heading">聯絡資訊</h2>
</section>
```

### 4. 使用 aria-hidden

隱藏裝飾性或重複的內容，避免屏幕閱讀器讀取：

```html
<div class="decorative-icon" aria-hidden="true">
  <!-- 裝飾性圖標 -->
</div>
```

### 5. 提供跳過導航連結

幫助鍵盤用戶快速跳到主要內容：

```html
<a href="#main-content" class="skip-link">跳至主要內容</a>
<main id="main-content">
  <!-- 主要內容 -->
</main>
```

### 6. 使用語義化 HTML 標籤

優先使用 HTML5 語義標籤，必要時再添加 ARIA：

```html
<!-- 好的做法 -->
<button>提交</button>

<!-- 避免這樣做 -->
<div role="button">提交</div>
```

### 7. 確保表單可訪問性

為表單控件添加適當的標籤和描述：

```html
<label for="email">電子郵件：</label>
<input 
  type="email" 
  id="email" 
  name="email"
  aria-required="true"
  aria-describedby="email-hint"
>
<span id="email-hint">請輸入有效的電子郵件地址</span>
```

## 本專案中的 WAI-ARIA 實現

在我們的 `index.html` 中，我們已經實現了以下 WAI-ARIA 功能：

1. **添加了跳過導航連結**
   ```html
   <a href="#main-content" class="skip-link">跳至主要內容</a>
   ```

2. **使用了 Landmark Roles**
   ```html
   <main id="main-content" role="main">
   <div class="hero" role="banner">
   <section class="contacts" aria-label="聯絡資訊">
   ```

3. **添加了 ARIA 標籤**
   ```html
   <a href="mailto:sharon05051991@gmail.com" aria-label="寄送郵件至 sharon05051991@gmail.com">
   ```

4. **隱藏了裝飾性內容**
   ```html
   <div class="overlay" aria-hidden="true"></div>
   ```

5. **添加了語義化標題**
   ```html
   <h2 class="sr-only">聯絡方式</h2>
   ```

## 測試工具

- **WAVE**：網頁可訪問性評估工具
- **axe DevTools**：瀏覽器擴展，用於自動化可訪問性測試
- **NVDA/JAWS**：屏幕閱讀器軟件
- **Lighthouse**：Chrome DevTools 中的審計工具

## 參考資源

- [W3C WAI-ARIA 規範](https://www.w3.org/TR/wai-aria/)
- [MDN Web Docs - ARIA](https://developer.mozilla.org/zh-TW/docs/Web/Accessibility/ARIA)
- [WebAIM - 使用 ARIA](https://webaim.org/techniques/aria/)
- [W3C PFWG](https://www.w3.org/WAI/PF/)

## 最佳實踐

1. **不要過度使用 ARIA**：只在必要時使用，優先使用語義化 HTML
2. **測試與驗證**：使用屏幕閱讀器和自動化工具測試
3. **保持更新**：關注 WAI-ARIA 規範的更新
4. **考慮所有用戶**：不僅僅是屏幕閱讀器用戶，還包括鍵盤用戶和認知障礙用戶

import React from 'react';

const Header: React.FC = () => {
  return (
    <header style={{
      backgroundColor: '#3f51b5',
      color: 'white',
      padding: '1rem',
      textAlign: 'center'
    }}>
      <h1 style={{
        margin: 0,
        fontSize: '1.5rem'
      }}>
        Weather App
      </h1>
    </header>
  );
};

export default Header;